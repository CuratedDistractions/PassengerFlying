##########################################################################################
# MAIN PANEL KNOBS
##########################################################################################

from lib.controls import Rotary

main_panel_knobs = []

# AirbusFBW/DUBrightness (0, 1, 2, 3)
du_brightness = [
    {
        "control_type": Rotary,
        "touchosc_address": "/multitoggle/",
        "xplane_dref_address": "AirbusFBW/DUBrightness",
        "xplane_dref_index": 0,
    },
    {
        "control_type": Rotary,
        "touchosc_address": "/multitoggle/",
        "xplane_dref_address": "AirbusFBW/DUBrightness",
        "xplane_dref_index": 1,
    },
    {
        "control_type": Rotary,
        "touchosc_address": "/multitoggle/",
        "xplane_dref_address": "AirbusFBW/DUBrightness",
        "xplane_dref_index": 2,
    },
    {
        "control_type": Rotary,
        "touchosc_address": "/multitoggle/",
        "xplane_dref_address": "AirbusFBW/DUBrightness",
        "xplane_dref_index": 3,
    },
]
main_panel_knobs.extend(du_brightness)
