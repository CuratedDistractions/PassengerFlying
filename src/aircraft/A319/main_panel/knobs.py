##########################################################################################
# MAIN PANEL KNOBS
##########################################################################################

from lib.controls import Rotary, Encoder, StepsRotary

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
        "touchosc_adjust_value": 0.025,
        "xplane_dref_address": "sim/cockpit2/gauges/actuators/barometer_setting_in_hg_pilot",
    },
]
main_panel_knobs.extend(isi_baro_setting_knob)

ns_knobs = [
    {
        "control_type": StepsRotary,
        "touchosc_address": "/rotary/cpt_rose",
        "xplane_dref_address": "AirbusFBW/NDmodeCapt",
    },
    {
        "control_type": StepsRotary,
        "touchosc_address": "/rotary/cpt_scale",
        "xplane_dref_address": "AirbusFBW/NDrangeCapt",
    },
]
main_panel_knobs.extend(ns_knobs)
