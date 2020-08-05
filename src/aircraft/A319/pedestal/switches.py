##########################################################################################
# PEDESTAL SWITCHES
##########################################################################################

from lib.controls import MultiToggle

UNDEFINED = "/undefined"
pedestal_switches = [
    # ckpt/doorLock[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "ckpt/doorLock",
    },
    # ckpt/door[1] (0 is door closed, 80 is door open)
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "ckpt/door",
    },
    # Engines
    # AirbusFBW/ENG1MasterSwitch[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/ENG1MasterSwitch",
    },
    # AirbusFBW/ENG2MasterSwitch[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/ENG2MasterSwitch",
    },
    # AirbusFBW/ENGModeSwitch[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/ENGModeSwitch",
    },
    # COM1
    # AirbusFBW/RMP1Switch[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/RMP1Switch",
    },
    # Transponder
    # AirbusFBW/XPDRTCASMode[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/XPDRTCASMode",
    },
    # AirbusFBW/XPDRSystem[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/XPDRSystem",
    },
    # AirbusFBW/XPDRTCASAltSelect[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/XPDRTCASAltSelect",
    },
    # Weather Radar
    # AirbusFBW/WXPowerSwitch[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "AirbusFBW/WXPowerSwitch",
    },
    # ckpt/ped/radar/gcs/anim[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "ckpt/ped/radar/gcs/anim",
    },
    # ckpt/ped/radar/manAuto/anim[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "ckpt/ped/radar/manAuto/anim",
    },
    # ckpt/radar/sys/anim[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "ckpt/radar/sys/anim",
    },
    # ckpt/ped/radar/pwr/anim[1]
    {
        "control_type": MultiToggle,
        "touchosc_address": UNDEFINED,
        "touchosc_horizontal": False,
        "xplane_dref_address": "ckpt/ped/radar/pwr/anim",
    },
    # Speedbrake armed?
    # ckpt/speedbrakeUp/anim
]
