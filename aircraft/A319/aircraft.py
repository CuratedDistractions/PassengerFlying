import logging

from aircraft.A319.controls import AirbusButton
from aircraft.A319.overhead_panel_labels import overhead_panel_labels
from aircraft.A319.overhead_panel_switches import overhead_panel_switches
from aircraft.A319.overhead_panel_buttons import overhead_panel_buttons
from lib.aircraft import BaseAircraft

# Create a logger object.
logger = logging.getLogger(__name__)


class Aircraft(BaseAircraft):
    def minimum_supported_version(self):
        return "0.1a"

    def maximum_supported_version(self):
        return "0.1a"

    def define_controls(self):
        # Add all labels
        for item in overhead_panel_labels:
            result = item["control_type"](**item)
            # logger.debug("Item: {}".format(item))
            self.add_control(result)

        # Add all switches (and knobs that act like switches)
        for item in overhead_panel_switches:
            result = item["control_type"](**item)
            self.add_control(result)

        # Add all buttons
        for item in overhead_panel_buttons:
            # logger.debug(item)
            result = item["control_type"](**item)
            self.add_control(result)

        # Use the IR1 light (which uses a button as background) to open ISCS screen
        iscs = AirbusButton(
            touchosc_address="/ovhd/push95",
            touchosc_initial_color="gray",
            xplane_command_address="toliss_airbus/iscs_open",
            remarks="ISCS Screen",
        )
        self.add_control(iscs)
