##########################################################################################
# MAIN PANEL SWITCHES
##########################################################################################

from aircraft.A319.controls import QnhSettingMultiToggle

main_panel_switches = []

# AirbusFBW/BaroUnitCapt
qnh_switch = [
    {
        "control_type": QnhSettingMultiToggle,
        "touchosc_address": "/multitoggle/cpt_qnh",
        "xplane_dref_address": "AirbusFBW/BaroUnitCapt",
        "touchosc_horizontal": True,
    },
]
main_panel_switches.extend(qnh_switch)
