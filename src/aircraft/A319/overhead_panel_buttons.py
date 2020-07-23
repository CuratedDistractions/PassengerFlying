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

calls_buttons = [
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/calls_mech",
        "xplane_command_address": "AirbusFBW/purser/mech",
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/calls_fwd",
        "xplane_command_address": "AirbusFBW/purser/fwd",
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/calls_aft",
        "xplane_command_address": "AirbusFBW/purser/aft",
    },
]
overhead_panel_buttons.extend(calls_buttons)

# AirbusFBW/FuelOHPArray[32]
fuel_pump_buttons = [
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/fuel_ltk_pumps_1",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/fuel_ltk_pumps_2",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/fuel_ctr_tk_1",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 2,
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/fuel_ctr_tk_2",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 3,
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/fuel_rtk_pumps_1",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 4,
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/fuel_rtk_pumps_2",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 5,
    },
]
overhead_panel_buttons.extend(fuel_pump_buttons)

apu_buttons = [
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/apu_master_sw",
        "xplane_dref_address": "AirbusFBW/APUMaster",
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/apu_start",
        "xplane_dref_address": "AirbusFBW/APUStarter",
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/apu_bleed",
        "xplane_dref_address": "AirbusFBW/APUBleedSwitch",
    },
]
overhead_panel_buttons.extend(apu_buttons)

# AirbusFBW/ElecOHPArray[16]
ElecOHPArray = [
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/ext_pwr",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 3,
    },
]
overhead_panel_buttons.extend(ElecOHPArray)

battery_buttons = [
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/elec_bat_1",
        "xplane_dref_address": "Unknown",
        "xplane_dref_index": 0,
    },
    {
        "control_type": AirbusButton,
        "touchosc_address": "/button/elec_bat_2",
        "xplane_dref_address": "Unknown",
        "xplane_dref_index": 0,
    },
]
overhead_panel_buttons.extend(battery_buttons)
