##########################################################################################
"""     OVERHEAD PANEL BUTTONS """
##########################################################################################

from aircraft.A319.controls import AirbusButton

# Some constants for TouchOSC
RED = "red"
GREEN = "green"
BLUE = "blue"
YELLOW = "yellow"
PURPLE = "purple"
GRAY = "gray"
GREY = "gray"
ORANGE = "orange"
BROWN = "brown"
PINK = "pink"

overhead_panel_buttons = []

# AirbusFBW/OHPLightsATA21
calls_buttons = [
    {
        "control_type": AirbusButton,
        "touchosc_address": "/ovhd/push93",
        "touchosc_color": GREY,
        "remarks": "CALLS MECH",
        "xplane_command_address": "AirbusFBW/purser/mech",
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/ovhd/push91",
        "touchosc_color": GREY,
        "remarks": "CALLS FWD",
        "xplane_command_address": "AirbusFBW/purser/fwd",
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/ovhd/push92",
        "touchosc_color": GREY,
        "remarks": "CALLS AFT",
        "xplane_command_address": "AirbusFBW/purser/aft",
    },
]
overhead_panel_buttons.extend(calls_buttons)

adr_buttons = [
    {
        "control_type": AirbusButton,
        "touchosc_address": "/ovhd/push98",
        "touchosc_color": GREY,
        "remarks": "ADR1",
        "xplane_dref_address": "AirbusFBW/ADRSwitchArray",
        "xplane_dref_index": 0,
    }
]
overhead_panel_buttons.extend(adr_buttons)
