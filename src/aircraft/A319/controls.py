import logging

from lib.controls import Label, MultiPush

# Create a logger object.
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


class AirbusSwitch(MultiPush):
    pass
