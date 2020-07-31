##########################################################################################
# OVERHEAD PANEL KNOBS
##########################################################################################

from lib.controls import Rotary

# AirbusFBW/OHPBrightnessLevel
overhead_panel_knobs = [
    {
        "control_type": Rotary,
        "touchosc_address": "/rotary/int_lt_ovhd_integ_lt",
        "xplane_dref_address": "AirbusFBW/OHPBrightnessLevel",
    },
]

# AirbusFBW/PackFlowSel[1]
    {
        "control_type": Rotary,
        "touchosc_address": "/UNDEFINED",
        "xplane_dref_address": "AirbusFBW/PackFlowSel",
    },
