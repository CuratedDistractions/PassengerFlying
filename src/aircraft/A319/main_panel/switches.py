##########################################################################################
# MAIN PANEL SWITCHES
##########################################################################################

from aircraft.A319.controls import AirbusQnhSettingMultiToggle

main_panel_switches = []

# AirbusFBW/BaroUnitCapt
qnh_switch = [
    {
        "control_type": AirbusQnhSettingMultiToggle,
        "touchosc_address": "/multitoggle/cpt_qnh",
        "xplane_dref_address": "AirbusFBW/BaroUnitCapt",
        "touchosc_horizontal": True,
    },
]
main_panel_switches.extend(qnh_switch)

# Chrono
# AirbusFBW/ClockETSwitch
# sim/instruments/timer_reset
# sim/instruments/timer_show_date
# sim/instruments/timer_start_stop
