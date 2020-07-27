##########################################################################################
# MAIN PANEL BUTTONS
##########################################################################################

from lib.controls import PushButton
from aircraft.A319.controls import AirbusQNHStandardButton

main_panel_buttons = []

master_buttons = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cpt_master_warning",
        "xplane_command_address": "sim/annunciator/clear_master_warning",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cpt_master_caution",
        "xplane_command_address": "sim/annunciator/clear_master_caution",
    },
]
main_panel_buttons.extend(master_buttons)

# AirbusFBW/BaroStdCapt
isi_baro_std_button = [
    {
        "control_type": AirbusQNHStandardButton,
        "touchosc_address": "/button/cpt_qnh",
        "xplane_dref_address": "AirbusFBW/BaroStdCapt",
    },
]
main_panel_buttons.extend(isi_baro_std_button)

chrono_button = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cpt_chrono",
        "xplane_command_address": "AirbusFBW/CaptChronoButton",
    },
]
main_panel_buttons.extend(chrono_button)

abrk_buttons = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/auto_brk_lo",
        "xplane_command_address": "AirbusFBW/AbrkLo",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/auto_brk_med",
        "xplane_command_address": "AirbusFBW/AbrkMed",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/auto_brk_max",
        "xplane_command_address": "AirbusFBW/AbrkMax",
    },
]
main_panel_buttons.extend(abrk_buttons)


# AirbusFBW/NDShowCSTRCapt[1]
# AirbusFBW/NDShowWPTCapt[1]
# AirbusFBW/NDShowVORDCapt[1]
# AirbusFBW/NDShowNDBCapt[1]
# AirbusFBW/NDShowARPTCapt[1]


# sim/autopilot/knots_mach_toggle
# AirbusFBW/APPRbutton
# AirbusFBW/ATHRbutton
# AirbusFBW/EXPEDbutton
# AirbusFBW/LOCbutton
# AirbusFBW/PullAltitude
# AirbusFBW/PullHDGSel
# AirbusFBW/PullSPDSel
# AirbusFBW/PullVSSel
# AirbusFBW/PushAltitude
# AirbusFBW/PushHDGSel
# AirbusFBW/PushSPDSel
# AirbusFBW/PushVSSel
# AirbusFBW/HDGTRKmode
