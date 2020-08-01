##########################################################################################
# PEDESTAL LABELS
##########################################################################################

from lib.controls import Label
from aircraft.A319.controls import AirbusLabel


# AirbusFBW/OHPLightsATA31[64] (also defined in overhead_panel_labels and main_panel_labels)
pedestal_labels = [
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 30,
        "touchosc_address": "/label/eng",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 31,
        "touchosc_address": "/label/bleed",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 32,
        "touchosc_address": "/label/press",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 33,
        "touchosc_address": "/label/elec",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 34,
        "touchosc_address": "/label/hyd",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 35,
        "touchosc_address": "/label/fuel",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 36,
        "touchosc_address": "/label/apu",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 37,
        "touchosc_address": "/label/cond",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 38,
        "touchosc_address": "/label/door",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 39,
        "touchosc_address": "/label/wheel",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 40,
        "touchosc_address": "/label/f_ctl",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 41,
        "touchosc_address": "/label/sts",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 42,
        "touchosc_address": "/label/clr_left",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 43,
        "touchosc_address": "/label/clr_right",
    },
    # AirbusFBW/ACP1Lights[16]
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/ACP1Lights",
        "xplane_dref_index": 0,
        "touchosc_address": "/label/cpt_com_call_1",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/ACP1Lights",
        "xplane_dref_index": 1,
        "touchosc_address": "/label/cpt_com_call_2",
    },
    # Transponder
    # AirbusFBW/XPDR1
    {"control_type": Label, "xplane_dref_address": "AirbusFBW/XPDR1", "touchosc_address": "/UNDEFINED",},
    # AirbusFBW/XPDR2
    {"control_type": Label, "xplane_dref_address": "AirbusFBW/XPDR2", "touchosc_address": "/UNDEFINED",},
    # AirbusFBW/XPDR3
    {"control_type": Label, "xplane_dref_address": "AirbusFBW/XPDR3", "touchosc_address": "/UNDEFINED",},
    # AirbusFBW/XPDR4
    {"control_type": Label, "xplane_dref_address": "AirbusFBW/XPDR4", "touchosc_address": "/UNDEFINED",},
    # These numbers are in reversed order
    # COM 1
    # AirbusFBW/RMP1StbyFreq[1]
    {"control_type": Label, "xplane_dref_address": "AirbusFBW/RMP1StbyFreq", "touchosc_address": "/UNDEFINED",},
    # AirbusFBW/RMP1Freq[1]
    {"control_type": Label, "xplane_dref_address": "AirbusFBW/RMP1Freq", "touchosc_address": "/UNDEFINED",},
]
