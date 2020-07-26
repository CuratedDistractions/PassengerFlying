import logging

from lib.settings import globals_list
from lib.controls import Label, MultiToggle

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
        # globals_list.qnh_setting = "hPa"  # Default setting

    def callback_from_xplane(self, results):
        text = results[self.xplane_dref_address][0]

        if globals_list.qnh_setting:
            text = round(text)
        else:
            text = text / 33.86
            text = "{:.2f}".format(text)

        self.touchosc_text = text


class QnhSettingMultiToggle(MultiToggle):
    def callback_from_touchosc(self, address, results):
        # logger.debug(results)
        if results > 0:  # 0 Means a button was deactivated. That should be ignored.
            # Extract which button of the multi control was pressed
            button_pressed = address.split("/")
            result = int(button_pressed[4]) - 1

            globals_list.qnh_setting = result

            # Send the whole dref back to X-Plane
            # logger.debug(f"Sending {result} to {self.xplane_dref_address}")
            self.send_to_xplane(self.xplane_dref_address, result)
