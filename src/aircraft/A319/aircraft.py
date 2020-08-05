import logging

from aircraft.A319.debug.buttons import debug_buttons
from aircraft.A319.main_panel.buttons import main_panel_buttons
from aircraft.A319.main_panel.knobs import main_panel_knobs
from aircraft.A319.main_panel.labels import main_panel_labels
from aircraft.A319.main_panel.switches import main_panel_switches
from aircraft.A319.main_panel.leds import main_panel_leds
# from aircraft.A319.other.buttons import other_buttons
from aircraft.A319.other.switches import other_switches
from aircraft.A319.overhead_panel.buttons import overhead_panel_buttons
from aircraft.A319.overhead_panel.guards import overhead_panel_guards
from aircraft.A319.overhead_panel.knobs import overhead_panel_knobs
from aircraft.A319.overhead_panel.labels import overhead_panel_labels
from aircraft.A319.overhead_panel.switches import overhead_panel_switches
from aircraft.A319.pedestal.buttons import pedestal_buttons
from aircraft.A319.pedestal.knobs import pedestal_knobs
from aircraft.A319.pedestal.labels import pedestal_labels
from aircraft.A319.pedestal.sliders import pedestal_sliders
from aircraft.A319.pedestal.switches import pedestal_switches
from lib.aircraft import BaseAircraft
from lib.controls import PushButton

# Create a logger object
logger = logging.getLogger(__name__)


class Aircraft(BaseAircraft):
    def minimum_supported_version(self):
        return "0.1a"

    def maximum_supported_version(self):
        return "0.1a"

    def define_controls(self):
        # Add all labels
        self.process_controls(overhead_panel_labels)
        self.process_controls(main_panel_labels)
        self.process_controls(pedestal_labels)

        # Add all switches (and knobs that act like switches)
        self.process_controls(overhead_panel_switches)
        self.process_controls(main_panel_switches)
        self.process_controls(pedestal_switches)
        self.process_controls(other_switches)

        # Add all buttons
        self.process_controls(overhead_panel_buttons)
        self.process_controls(main_panel_buttons)
        self.process_controls(pedestal_buttons)

        # Add all LEDs
        self.process_controls(main_panel_leds)

        # Add all guards
        self.process_controls(overhead_panel_guards)

        # Add all sliders
        self.process_controls(pedestal_sliders)

        # Add all knobs
        self.process_controls(overhead_panel_knobs)
        self.process_controls(main_panel_knobs)
        self.process_controls(pedestal_knobs)

        # Add debug buttons
        self.process_controls(debug_buttons)

        # Use the IR1 light (which uses a button as background) to open ISCS screen
        iscs = PushButton(touchosc_address="/ovhd/push95", xplane_command_address="toliss_airbus/iscs_open",)
        self.add_control(iscs)

    def process_controls(self, controls):
        for item in controls:
            result = item["control_type"](**item)
            self.add_control(result)
