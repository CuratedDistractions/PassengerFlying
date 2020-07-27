##########################################################################################
# OVERHEAD PANEL KNOBS
##########################################################################################

from lib.controls import Rotary

overhead_panel_knobs = []

# AirbusFBW/OHPBrightnessLevel
du_brightness = [
    {
        "control_type": Rotary,
        "touchosc_address": "/rotary/int_lt_ovhd_integ_lt",
        "xplane_dref_address": "AirbusFBW/OHPBrightnessLevel",
    },
]
overhead_panel_knobs.extend(du_brightness)

# AirbusFBW/PackFlowSel[1]
