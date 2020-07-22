##########################################################################################
"""     OVERHEAD PANEL SWITCHES """
##########################################################################################

from aircraft.A319.controls import AirbusSwitch

overhead_panel_switches = []

adiru_switch_array = [
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/ir1",
        "touchosc_horizontal": False,
        "remarks": "IR 1",
        "xplane_dref_address": "AirbusFBW/ADIRUSwitchArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/ir3",
        "touchosc_horizontal": False,
        "remarks": "IR 2",
        "xplane_dref_address": "AirbusFBW/ADIRUSwitchArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/ir2",
        "touchosc_horizontal": False,
        "remarks": "IR 3",
        "xplane_dref_address": "AirbusFBW/ADIRUSwitchArray",
        "xplane_dref_index": 2,
    },
]
overhead_panel_switches.extend(adiru_switch_array)

OHPLightSwitches = [
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/ext_lt_beacon",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 0,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/ext_lt_wing",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 1,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/ext_lt_nav_logo",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 2,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/ext_lt_nose",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 3,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/ext_lt_land_l",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 4,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/ext_lt_land_r",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 5,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/ext_lt_rwy_turn_off",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 6,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/ext_lt_strobe",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 7,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/int_lt_dome",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 8,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/int_lt_stby_compass",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 9,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/emer_exit_lt",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 10,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/seat_belts",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 11,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/multitoggle/no_smoking",
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/OHPLightSwitches",
        "xplane_dref_index": 12,
    },
]
overhead_panel_switches.extend(OHPLightSwitches)

int_lt_ann_lt = [{
    "control_type": AirbusSwitch,
    "touchosc_address": "/multitoggle/int_lt_ann_lt",
    "touchosc_horizontal": False,
    "xplane_dref_address": "AirbusFBW/AnnunMode",
}]
overhead_panel_switches.extend(int_lt_ann_lt)

# wiper_left = WiperKnob(
#     name:"Wiper Left",
#     xplane_dref="AirbusFBW/LeftWiperSwitch",
#  {   index ,
#     address:"/multitoggle/wiper_left",
#     color:GREY,
#     visible:True,
#     name:"WIPER L",
#     debug=True,},
# )
# self.add_control(wiper_left)

# wiper_right = WiperKnob(
#     name:"Wiper Right",
#     xplane_dref="AirbusFBW/RightWiperSwitch",
#  {   index ,
#     address:"/multitoggle/wiper_right/1/1",
#     color:GREY,
#     visible:True,
#     name:"WIPER R",
#     debug=True,},
# )
# self.add_control(wiper_right)
