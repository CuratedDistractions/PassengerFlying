##########################################################################################
"""     OVERHEAD PANEL SWITCHES """
##########################################################################################

from aircraft.A319.controls import AirbusSwitch

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

overhead_panel_switches = []


adiru_switch_array = [
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/ovhd/multitoggle3",
        "touchosc_initial_color": GREY,
        "touchosc_horizontal": False,
        "remarks": "AR 1",
        "xplane_dref_address": "AirbusFBW/ADIRUSwitchArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/ovhd/multitoggle5",
        "touchosc_initial_color": GREY,
        "touchosc_horizontal": False,
        "remarks": "IR 2",
        "xplane_dref_address": "AirbusFBW/ADIRUSwitchArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": AirbusSwitch,
        "touchosc_address": "/ovhd/multitoggle4",
        "touchosc_initial_color": GREY,
        "touchosc_horizontal": False,
        "remarks": "IR 3",
        "xplane_dref_address": "AirbusFBW/ADIRUSwitchArray",
        "xplane_dref_index": 2,
    },
]

overhead_panel_switches.extend(adiru_switch_array)

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
