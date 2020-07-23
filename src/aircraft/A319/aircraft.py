import logging

from aircraft.A319.controls import AirbusButton
from aircraft.A319.overhead_panel_buttons import overhead_panel_buttons
from aircraft.A319.overhead_panel_labels import overhead_panel_labels
from aircraft.A319.overhead_panel_switches import overhead_panel_switches
from aircraft.A319.main_panel_buttons import main_panel_buttons
from aircraft.A319.main_panel_labels import main_panel_labels
from aircraft.A319.main_panel_switches import main_panel_switches
from aircraft.A319.pedestal_buttons import pedestal_buttons
from aircraft.A319.pedestal_labels import pedestal_labels
from aircraft.A319.pedestal_switches import pedestal_switches
from aircraft.A319.debug_buttons import debug_buttons
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
            self.add_control(result)

        for item in main_panel_labels:
            result = item["control_type"](**item)
            self.add_control(result)

        for item in pedestal_labels:
            result = item["control_type"](**item)
            self.add_control(result)

        # Add all switches (and knobs that act like switches)
        for item in overhead_panel_switches:
            result = item["control_type"](**item)
            self.add_control(result)

        for item in main_panel_switches:
            result = item["control_type"](**item)
            self.add_control(result)

        for item in pedestal_switches:
            result = item["control_type"](**item)
            self.add_control(result)

        # Add all buttons
        for item in overhead_panel_buttons:
            result = item["control_type"](**item)
            self.add_control(result)

        for item in main_panel_buttons:
            result = item["control_type"](**item)
            self.add_control(result)

        for item in pedestal_buttons:
            result = item["control_type"](**item)
            self.add_control(result)

        for item in debug_buttons:
            result = item["control_type"](**item)
            self.add_control(result)

        # Use the IR1 light (which uses a button as background) to open ISCS screen
        iscs = AirbusButton(touchosc_address="/ovhd/push95", xplane_command_address="toliss_airbus/iscs_open",)
        self.add_control(iscs)
