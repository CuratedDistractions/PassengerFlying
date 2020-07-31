##########################################################################################
# OVERHEAD PANEL SWITCHES
##########################################################################################

from lib.controls import MultiToggle

# AirbusFBW/ADIRUSwitchArray[6]
overhead_panel_switches = [
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/adirs_ir1",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/ADIRUSwitchArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/adirs_ir3",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/ADIRUSwitchArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/adirs_ir2",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/ADIRUSwitchArray",
        "xplane_dref_index": 2,
    },
    # AirbusFBW/OHPLightSwitches[16]
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/ext_lt_beacon",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",  # toliss_airbus/lightcommands/BeaconToggle
        "xplane_dref_index": 0,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/ext_lt_wing",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",  # toliss_airbus/lightcommands/WingLightToggle
        "xplane_dref_index": 1,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/ext_lt_nav_logo",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 2,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/ext_lt_nose",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 3,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/ext_lt_land_l",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 4,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/ext_lt_land_r",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 5,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/ext_lt_rwy_turn_off",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",  # toliss_airbus/lightcommands/TurnoffLightToggle
        "xplane_dref_index": 6,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/ext_lt_strobe",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 7,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/int_lt_dome",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 8,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/int_lt_stby_compass",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",  # toliss_airbus/lightcommands/CompassLightToggle
        "xplane_dref_index": 9,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/emer_exit_lt",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 10,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/seat_belts",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 11,
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/no_smoking",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",  # toliss_airbus/lightcommands/FSBSignToggle
        "xplane_dref_index": 12,
    },
    # Test lights
    {
        "control_type": MultiToggle,
        "touchosc_address": "/multitoggle/int_lt_ann_lt",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/AnnunMode",
    },
    # Wipers
    {
        "control_type": MultiToggle,
        "touchosc_address": "/UNDEFINED",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/LeftWiperSwitch",
    },
    {
        "control_type": MultiToggle,
        "touchosc_address": "/UNDEFINED",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/RightWiperSwitch",
    },
]
