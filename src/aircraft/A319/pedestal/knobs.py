##########################################################################################
# PEDESTAL KNOBS
##########################################################################################

from lib.controls import Encoder

pedestal_knobs = []

# AirbusFBW/PanelFloodBrightnessLevel

# AirbusFBW/PanelBrightnessLevel

# AirbusFBW/PedestalFloodBrightnessLevel

# AirbusFBW/DUBrightness (4, 5, 6, 7)

# AirbusFBW/ISIBaroSetting
isi_baro_setting_knob = [
    {
        "control_type": Encoder,
        "touchosc_address": "/encoder/cpt_qnh_backup",
        "xplane_dref_address": "AirbusFBW/ISIBaroSetting",
    },
]
pedestal_knobs.extend(isi_baro_setting_knob)

# Transponder
# AirbusFBW/XPDRPower
