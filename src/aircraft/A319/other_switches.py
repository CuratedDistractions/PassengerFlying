##########################################################################################
""" OTHER SWITCHES """
##########################################################################################

from aircraft.A319.controls import AirbusSwitch
import logging

# Create a logger object.
logger = logging.getLogger(__name__)

other_switches = []

# AirbusFBW/CargoDoorModeArray[2] // All values checked
cargo_door_mode_array = [
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/cargo_door_1",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/ADIRUSwitchArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/cargo_door_2",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/ADIRUSwitchArray",
        "xplane_dref_index": 1,
    },
]
other_switches.extend(cargo_door_mode_array)

# AirbusFBW/PaxDoorModeArray[4] // All values checked
pax_door_mode_array = [
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/pax_door_1",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/PaxDoorModeArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/pax_door_2",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/PaxDoorModeArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/pax_door_3",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/PaxDoorModeArray",
        "xplane_dref_index": 2,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/pax_door_4",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/PaxDoorModeArray",
        "xplane_dref_index": 3,
    },
]
other_switches.extend(pax_door_mode_array)
