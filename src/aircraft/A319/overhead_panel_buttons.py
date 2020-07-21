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
        "touchosc_address": "/button/calls_mech",
        "touchosc_initial_color": GREY,
        "remarks": "CALLS MECH",
        "xplane_command_address": "AirbusFBW/purser/mech",
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/calls_fwd",
        "touchosc_initial_color": GREY,
        "remarks": "CALLS FWD",
        "xplane_command_address": "AirbusFBW/purser/fwd",
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/calls_aft",
        "touchosc_initial_color": GREY,
        "remarks": "CALLS AFT",
        "xplane_command_address": "AirbusFBW/purser/aft",
    },
]
overhead_panel_buttons.extend(calls_buttons)

adr_buttons = [
    {
        "control_type": AirbusButton,
        "touchosc_address": "/ovhd/push98",
        "touchosc_initial_color": GREY,
        "remarks": "ADR1",
        "xplane_dref_address": "AirbusFBW/ADRSwitchArray",
        "xplane_dref_index": 0,
    }
]
overhead_panel_buttons.extend(adr_buttons)

fuel_pump_buttons = [
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/ltk_pumps_1",
        "touchosc_initial_color": GREY,
        "remarks": "LTK PUMPS 1",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/ltk_pumps_2",
        "touchosc_initial_color": GREY,
        "remarks": "LTK PUMPS 2",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/ctr_tk_2",
        "touchosc_initial_color": GREY,
        "remarks": "CTR TK 1",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 2,
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/ctr_tk_2",
        "touchosc_initial_color": GREY,
        "remarks": "CTR TK 2",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 3,
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/rtk_pumps_1",
        "touchosc_initial_color": GREY,
        "remarks": "RTK PUMPS 1",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 4,
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/rtk_pumps_2",
        "touchosc_initial_color": GREY,
        "remarks": "RTK PUMPS 2",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 5,
    },
]
overhead_panel_buttons.extend(fuel_pump_buttons)

apu_buttons = [
    {
        "control_type": AirbusButton,
        "touchosc_address": "/apu_master_sw",
        "touchosc_initial_color": GREY,
        "remarks": "APU MASTER SW",
        "xplane_dref_address": "AirbusFBW/APUMaster",
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/apu_start",
        "touchosc_initial_color": GREY,
        "remarks": "APU START",
        "xplane_dref_address": "AirbusFBW/APUStarter",
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/apu_bleed",
        "touchosc_initial_color": GREY,
        "remarks": "APU BLEED",
        "xplane_dref_address": "AirbusFBW/APUBleedSwitch",
    },
]
overhead_panel_buttons.extend(apu_buttons)

external_power_button = [
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/ext_pwr",
        "touchosc_initial_color": GREY,
        "remarks": "EXT PWR",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 3,
    },
]
overhead_panel_buttons.extend(external_power_button)
