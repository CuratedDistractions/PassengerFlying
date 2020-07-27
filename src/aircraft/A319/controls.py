import logging

from lib.settings import globals_list
from lib.controls import Label, MultiToggle, PushButton
from lib.xplane import get_from_xplane

# Create a logger object
logger = logging.getLogger(__name__)


class AirbusLabel(Label):
    def callback_from_xplane(self, results):
        if self.xplane_dref_address:
            if self.xplane_dref_index is not None:
                result = results[self.xplane_dref_address][self.xplane_dref_index]
            else:
                result = results[self.xplane_dref_address]

            state = self.__is_on(result)
            self.touchosc_visible = state

    @staticmethod
    def __is_on(value):
        if value < 0.2:
            return 0  # Light is off
        else:
            return 1  # Light is on


class AirbusQNHLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        globals_list.qnh_setting_hpa = True  # Default setting

    def callback_from_xplane(self, results):
        text = results[self.xplane_dref_address][0]

        if globals_list.qnh_standard:
            text = "Std"
        elif globals_list.qnh_setting_hpa:
            # logger.debug(f"hPa: {globals_list.qnh_setting_hpa}")
            text = round(text)
        else:
            # logger.debug(f"inHg: {globals_list.qnh_setting_hpa}")
            text = text / 33.86
            text = "{:.2f}".format(text)

        self.touchosc_text = text


class AirbusQnhSettingMultiToggle(MultiToggle):
    def callback_from_touchosc(self, address, results):
        # logger.debug(results)
        if results > 0:  # 0 Means a button was deactivated. That should be ignored.
            # Extract which button of the multi control was pressed
            button_pressed = address.split("/")
            result = int(button_pressed[4]) - 1

            globals_list.qnh_setting_hpa = result

            # Send the whole dref back to X-Plane
            self.send_to_xplane(self.xplane_dref_address, result)

    def callback_from_xplane(self, results):
        result = results[self.xplane_dref_address][0]
        state = int(result) + 1

        globals_list.qnh_setting_hpa = int(result)
        self.touchosc_state = state


class AirbusQNHStandardButton(PushButton):
    def callback_from_touchosc(self, address, results):
        if results > 0:  # We ignore the release of the button
            # Get the current dref value.
            xplane_dref_value = list(get_from_xplane(self.xplane_dref_address))[0]

            # Toggle
            xplane_dref_value = int(not xplane_dref_value)
            globals_list.qnh_standard = xplane_dref_value

            # Send the whole dref back to X-Plane
            self.send_to_xplane(self.xplane_dref_address, xplane_dref_value)

    def callback_from_xplane(self, results):
        result = results[self.xplane_dref_address][0]
        globals_list.qnh_standard = result

