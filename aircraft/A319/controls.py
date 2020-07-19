import logging

from lib.controls import Label, MultiPush, PushButton

# Create a logger object.
logger = logging.getLogger(__name__)


class AirbusButton(PushButton):
    """The buttons on the Airbus often have two lights on them. Each with a word and a (different) color."""

    pass


class AirbusButtonLabel(Label):
    def callback_from_xplane(self, results):
        if self.xplane_dref_address:
            result = results[self.xplane_dref_address][self.xplane_dref_index]
            previous_state = self.touchosc_visible
            state = self.is_on(result)
            if state != previous_state:
                self.touchosc_visible = state

    def is_on(self, value):
        if value < 0.2:
            return 0  # Light is off
        else:
            return 1  # Light is on


class AirbusSwitch(MultiPush):
    def callback_from_touchosc(self, touchosc_address, touchosc_results):
        logger.debug(f"Results from TouchOSC: {touchosc_results}")
        if touchosc_results > 0:  # 0 Means a button was deactivated. But that is of no value to us with a multi control
            # Extract which button of the multi control was pressed
            if self.touchosc_horizontal:
                logger.debug("Processing for touchosc_address {}".format(touchosc_address))
