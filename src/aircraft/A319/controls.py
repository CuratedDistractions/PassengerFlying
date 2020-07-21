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
            if self.xplane_dref_index is not None:
                result = results[self.xplane_dref_address][self.xplane_dref_index]
                state = self.is_on(result)
                self.touchosc_visible = state
            else:
                logger.debug("Nothing to do for this label")

    def is_on(self, value):
        if value < 0.2:
            return 0  # Light is off
        else:
            return 1  # Light is on


class AirbusSwitch(MultiPush):
    pass
