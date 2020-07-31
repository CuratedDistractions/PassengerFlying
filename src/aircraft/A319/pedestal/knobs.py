##########################################################################################
# PEDESTAL KNOBS
##########################################################################################

from lib.controls import Encoder

pedestal_knobs = [
    # AirbusFBW/PanelFloodBrightnessLevel
    {
        "control_type": Encoder,
        "touchosc_address": "/UNDEFINED",
        "xplane_dref_address": "AirbusFBW/PanelFloodBrightnessLevel",
    },
    # AirbusFBW/PanelBrightnessLevel
    {
        "control_type": Encoder,
        "touchosc_address": "/UNDEFINED",
        "xplane_dref_address": "AirbusFBW/PanelBrightnessLevel",
    },
    # AirbusFBW/PedestalFloodBrightnessLevel
    {
        "control_type": Encoder,
        "touchosc_address": "/UNDEFINED",
        "xplane_dref_address": "AirbusFBW/PedestalFloodBrightnessLevel",
    },
    # AirbusFBW/DUBrightness (4, 5, 6, 7)
    {
        "control_type": Encoder,
        "touchosc_address": "/UNDEFINED",
        "xplane_dref_address": "AirbusFBW/DUBrightness",
    },
    # AirbusFBW/ISIBaroSetting
    {
        "control_type": Encoder,
        "touchosc_address": "/UNDEFINED",
        "xplane_dref_address": "AirbusFBW/ISIBaroSetting",
    },
    # Transponder
    # AirbusFBW/XPDRPower[1]
    {
        "control_type": Encoder,
        "touchosc_address": "/UNDEFINED",
        "xplane_dref_address": "AirbusFBW/XPDRPower",
    },
    # Weather
    # ckpt/fped/radar/gain/ani[1]
    {
        "control_type": Encoder,
        "touchosc_address": "/UNDEFINED",
        "xplane_dref_address": "ckpt/fped/radar/gain/ani",
    },
    # ckpt/fped/radar/mode/anim[1]
    {
        "control_type": Encoder,
        "touchosc_address": "/UNDEFINED",
        "xplane_dref_address": "ckpt/fped/radar/mode/anim",
    },
    # ckpt/fped/radar/tilt/anim[1]
    {
        "control_type": Encoder,
        "touchosc_address": "/UNDEFINED",
        "xplane_dref_address": "ckpt/fped/radar/tilt/anim",
    },
]
