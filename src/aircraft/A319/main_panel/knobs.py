##########################################################################################
# MAIN PANEL KNOBS
##########################################################################################

from lib.controls import Rotary, Encoder

main_panel_knobs = []

# AirbusFBW/DUBrightness (0, 1, 2, 3)
du_brightness_knobs = [
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
main_panel_knobs.extend(du_brightness_knobs)

# AirbusFBW/ISIBaroSetting
isi_baro_setting_knob = [
    {
        "control_type": Encoder,
        "touchosc_address": "/encoder/cpt_qnh",
        "xplane_dref_address": "AirbusFBW/ISIBaroSetting",
        "xplane_dref_index": 0,
    },
]
main_panel_knobs.extend(isi_baro_setting_knob)
