"""
Source of descriptions: https://hexler.net/docs/touchosc-controls-reference
"""
import logging
import lib.settings as settings

# Create a logger object.
logger = logging.getLogger(__name__)

# List of colors TouchOSC supports
TOUCHOSC_COLORS = [
    "red",
    "green",
    "blue",
    "yellow",
    "purple",
    "gray",
    "orange",
    "brown",
    "pink",
]

touchosc = settings.globalList["TOUCHOSC"]
xplane = settings.globalList["XPLANE"]


class TouchoscControlItem:
    """This is the base class for all TouchOSC controls."""

    def __init__(
        self,
        control_type=None,  # Optional, can be used when adding controls in batches
        touchosc_address: str = None,
        touchosc_initial_color: str = None,
        touchosc_visible: bool = True,
        xplane_dref_address: str = None,
        xplane_dref_index: int = None,
        xplane_command_address: str = None,
        remarks: str = None,
    ):
        # Initialize some variables
        self._touchosc_color = None
        self._touchosc_visible = None

        self.touchosc_address = touchosc_address
        if touchosc_address:
            settings.globalList["FORCE_REFRESH"][self.touchosc_address] = False
        if touchosc_initial_color:
            self.touchosc_color = touchosc_initial_color
        self.touchosc_visible = touchosc_visible
        self.xplane_dref_address = xplane_dref_address
        self.xplane_dref_index = xplane_dref_index
        self.xplane_command_address = xplane_command_address
        self.remarks = remarks

    def callback_from_xplane(self, results):
        pass

    def callback_from_touchosc(self, address, results):
        # Always provide the TouchOSC address. It's used for Multi* controls.
        pass

    @property
    def touchosc_color(self):
        """Color of an item in TouchOSC"""
        return self._touchosc_color

    @touchosc_color.setter
    def touchosc_color(self, value):
        """Sets the color of an item in TouchOSC and checks for valid color values"""
        # Do nothing if value wasn't changed and no force refresh needed
        force_refresh = settings.globalList["FORCE_REFRESH"][self.touchosc_address]
        if value == self._touchosc_color and not force_refresh:
            return

        if value in TOUCHOSC_COLORS:
            self._touchosc_color = value
            self.set_color_in_touchosc()
        else:
            logger.warning(f"Tried to set color {value} for {self.touchosc_address}, which is not supported.")

        settings.globalList["FORCE_REFRESH"][self.touchosc_address] = False

    @property
    def touchosc_visible(self):
        """Visibility of an item in TouchOSC"""
        try:
            return self._touchosc_visible
        except AttributeError:
            return True

    @touchosc_visible.setter
    def touchosc_visible(self, value: bool):
        """Sets the visibility of an item in TouchOSC"""
        # Do nothing if value wasn't changed and no force refresh needed
        force_refresh = settings.globalList["FORCE_REFRESH"][self.touchosc_address]
        if value == self._touchosc_visible and not force_refresh:
            return

        if self.touchosc_address:
            self._touchosc_visible = value
            self.set_visibility_in_touchosc()

        settings.globalList["FORCE_REFRESH"][self.touchosc_address] = False


    @property
    def touchosc_address(self):
        """Optional control to listen for or send commands to in TouchOSC"""
        return self._touchosc_address

    @touchosc_address.setter
    def touchosc_address(self, value: str):
        """Optional control to listen for or send commands to in TouchOSC"""
        self._touchosc_address = value

    @property
    def xplane_dref_address(self) -> str:
        """Optional dref to listen for or send commands to in X-Plane"""
        return self._xplane_dref_address

    @xplane_dref_address.setter
    def xplane_dref_address(self, value: str):
        """Optional dref to listen for or send commands to in X-Plane"""
        self._xplane_dref_address = value

    @property
    def xplane_dref_index(self) -> int:
        """Optional dref to listen for or send commands to in X-Plane, this is its index number"""
        return self._xplane_dref_index

    @xplane_dref_index.setter
    def xplane_dref_index(self, value: int):
        """Optional dref to listen for or send commands to in X-Plane, this is its index number"""
        self._xplane_dref_index = value

    @property
    def xplane_command_address(self) -> str:
        """Optional command to send to X-Plane"""
        return self._xplane_command_address

    @xplane_command_address.setter
    def xplane_command_address(self, value: str):
        """Optional command to send to X-Plane"""
        self._xplane_command_address = value

    def set_color_in_touchosc(self):
        """Actual command to set color in TouchOSC"""
        address = "/".join([str(self.touchosc_address), "color"])
        self.send_to_touchosc(address, self.touchosc_color)

    def set_visibility_in_touchosc(self):
        """Actual command to set visibility in TouchOSC"""
        address = "/".join([self.touchosc_address, "visible"])
        self.send_to_touchosc(address, self.touchosc_visible)

    @staticmethod
    def send_to_touchosc(address, value):
        touchosc.send_to_touchosc(address, value)

    @staticmethod
    def send_to_xplane(address, value=None):
        xplane.send_to_xplane(address, value)


class Label(TouchoscControlItem):
    def __init__(self, touchosc_initial_text: str = None, **kwargs):
        super().__init__(**kwargs)
        self._touchosc_text = None
        if touchosc_initial_text:
            self.touchosc_text = touchosc_initial_text

    @property
    def touchosc_text(self) -> str:
        """The text of the label in TouchOSC"""
        try:
            return self._touchosc_text
        except AttributeError:
            return "LABEL"

    @touchosc_text.setter
    def touchosc_text(self, value: str):
        """The text of the label in TouchOSC"""
        # Do nothing if value wasn't changed and no force refresh needed
        force_refresh = settings.globalList["FORCE_REFRESH"][self.touchosc_address]
        if value == self._touchosc_text and not force_refresh:
            return

        self._touchosc_text = value
        self.__set_touchosc_label_text()

        settings.globalList["FORCE_REFRESH"][self.touchosc_address] = False

    def __set_touchosc_label_text(self):
        """The actual command to set the text of a label in TouchOSC"""
        self.send_to_touchosc(self.touchosc_address, self.touchosc_text)


class DynamicLabel(Label):
    """Will change the text of the label to the value reported by X-Plane"""

    def callback_from_xplane(self, results):
        if self.xplane_dref_address:
            if self.xplane_dref_index is not None:
                text = results[self.xplane_dref_address][self.xplane_dref_index]
            else:
                text = results[self.xplane_dref_address]

            if type(text) == float:
                text = "{:.1f}".format(text)

            self.touchosc_text = text


class Led(TouchoscControlItem):
    """This control is for display purposes only and does not react to touch or send messages.

    Values of incoming messages are mapped to the control's value range and update the brightness of the LED display.
    """

    pass


class PushButton(TouchoscControlItem):
    """This control sends the second value of its value range when pressed and the first value of its value range when released."""

    def callback_from_touchosc(self, address, results):
        if results > 0:  # We ignore the release of the button
            if self.xplane_command_address:  # If no command address was defined, we'll use the dref address
                self.send_to_xplane(self.xplane_command_address)
            else:
                if self.xplane_dref_index is not None:  # Does the dref contain an array
                    # Get the whole dref. Since it's a tuple, we need to convert it to a list
                    xplane_dref_value = list(xplane.get_from_xplane(self.xplane_dref_address))

                    # Replace just the index we need (it's a toggle)
                    xplane_dref_value[self.xplane_dref_index] = int(not xplane_dref_value[self.xplane_dref_index])
                else:
                    # Get the current dref value.
                    xplane_dref_value = list(xplane.get_from_xplane(self.xplane_dref_address))[0]

                    # Toggle
                    xplane_dref_value = int(not xplane_dref_value)

                # Send the whole dref back to X-Plane
                self.send_to_xplane(self.xplane_dref_address, xplane_dref_value)


class ToggleButton(TouchoscControlItem):
    """This control changes state between on/off when released. When the state changes to on, the second value in it's value range is sent, otherwise the first."""

    pass


class XYPad(TouchoscControlItem):
    """This control maps the position of a touch along the x and y axes of its rectangle to its value range and sends out both values. Both x and y values use the same value range. The location of the minimum and maximum value positions of each axes can be inverted in the control's properties."""

    pass


class Fader(TouchoscControlItem):
    """These controls emulate classic fader and potentiometer controls on hardware devices. They map the position of a touch to their value range by interpolating between their minimum and maximum positions."""

    pass


class Rotary(TouchoscControlItem):
    """This control emulates an endless rotary or encoder control on hardware devices. It sends the upper end of its value range when a touch is moved clockwise, the lower end of its value range when a touch is moved counter-clockwise. It does not respond to incoming messages."""

    pass


class Encoder(TouchoscControlItem):
    """This control emulates an endless rotary or encoder control on hardware devices. It sends the upper end of its value range when a touch is moved clockwise, the lower end of its value range when a touch is moved counter-clockwise. It does not respond to incoming messages."""

    pass


class Battery(TouchoscControlItem):
    """This control is for display purposes only and does not react to touch or send messages. It displays the current battery charge of the device. It does not respond to incoming messages."""

    pass


class Time(TouchoscControlItem):
    """This control is for display purposes only and does not react to touch or send messages. It displays the current time. It does not respond to incoming messages."""

    pass


class MultiToggle(TouchoscControlItem):
    """This control groups multiple toggle controls into one control. A touch event can traverse multiple toggle controls in one gesture and change their values. This control accepts multiple touch events at the same time."""


class MultiXY(TouchoscControlItem):
    """This control behaves the same way as the XY Pad control but handles up to 5 touch-points at the same time. This control accepts multiple touch events. It does not respond to incoming messages."""

    pass


class MultiPush(TouchoscControlItem):
    """This control groups multiple push-button controls into one control. A touch event can traverse multiple push controls in one gesture and change their values. This control accepts multiple touch events at the same time."""

    # This version assumes the control is set to exclusive (only one item active at a time)
    def __init__(self, touchosc_horizontal=None, **kwargs):
        super().__init__(**kwargs)
        self.touchosc_horizontal = touchosc_horizontal
        self._touchosc_state = None

    @property
    def touchosc_address(self):
        """Optional control to listen for or send commands to in TouchOSC"""
        return self._touchosc_address

    @touchosc_address.setter
    def touchosc_address(self, value: str):
        """Optional control to listen for or send commands to in TouchOSC"""
        # Add a * to the end of the address to listen for all buttons in the MultiPush control
        # ? Why add a * here? I forgot why. :)
        if value[-1:] == "*":
            self._touchosc_address = value
        else:
            self._touchosc_address = value + "*"

    @property
    def touchosc_state(self):
        return self._touchosc_state

    @touchosc_state.setter
    def touchosc_state(self, value: int):
        # Do nothing if nothing changed and no force refresh needed
        force_refresh = settings.globalList["FORCE_REFRESH"][self.touchosc_address]
        if self._touchosc_state == value and not force_refresh:
            return

        """The text of the label in TouchOSC"""
        self._touchosc_state = value
        self.__set_state_in_touchosc()

        settings.globalList["FORCE_REFRESH"][self.touchosc_address] = False

    def __set_state_in_touchosc(self):
        """The actual command to set the state in TouchOSC"""
        # Build the TouchOSC address
        if self.touchosc_horizontal:
            address = self.touchosc_address + "/1/" + str(self.touchosc_state)
        else:
            address = self.touchosc_address + "/" + str(self.touchosc_state) + "/1"
        self.send_to_touchosc(address, 1)

    def callback_from_xplane(self, results):
        if self.xplane_dref_address:
            state = int(results[self.xplane_dref_address][self.xplane_dref_index]) + 1
            self.touchosc_state = state

    def callback_from_touchosc(self, results):
        logger.debug(f"Results from TouchOSC: {results}")
        if results > 0:  # 0 Means a button was deactivated. That should be ignored.
            # Extract which button of the multi control was pressed
            if self.touchosc_horizontal:
                logger.debug("Processing horizontal switch for touchosc_address {}".format(self.touchosc_address))
            else:
                logger.debug("Processing vertical switch for touchosc_address {}".format(self.touchosc_address))
                button_pressed = results.split("/")
                logger.debug(button_pressed)


class MultiFader(TouchoscControlItem):
    """This control groups multiple fader controls into one control. A touch event can traverse multiple fader controls in one gesture and change their values. This control accepts multiple touch events at the same time."""

    pass
