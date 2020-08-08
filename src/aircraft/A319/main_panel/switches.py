##########################################################################################
# MAIN PANEL SWITCHES
##########################################################################################

from aircraft.A319.controls import AirbusQnhSettingMultiToggle
from lib.controls import MultiToggle

main_panel_switches = [
    # AirbusFBW/BaroUnitCapt
    {
        "control_type": AirbusQnhSettingMultiToggle,
        "touchosc_address": "/multitoggle/cpt_qnh",
        "xplane_dref_address": "AirbusFBW/BaroUnitCapt",
        "touchosc_horizontal": True,
    },
    # Chrono
    # AirbusFBW/ClockETSwitch
    {
        "control_type": MultiToggle,
        "touchosc_address": "/NOT_DEFINED",
        "xplane_dref_address": "AirbusFBW/ClockETSwitch",
        "touchosc_horizontal": False,
    },
    # AirbusFBW/ALT100_1000
    {
        "control_type": MultiToggle,
        "touchosc_address": "/NOT_DEFINED",
        "xplane_dref_address": "AirbusFBW/ALT100_1000",
        "touchosc_horizontal": False,
    },
]
