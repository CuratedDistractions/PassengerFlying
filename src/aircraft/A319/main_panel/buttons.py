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


nd_show_buttons = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cpt_cstr",
        "xplane_dref_address": "AirbusFBW/NDShowCSTRCapt",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cpt_wpt",
        "xplane_dref_address": "AirbusFBW/NDShowWPTCapt",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cpt_vor_d",
        "xplane_dref_address": "AirbusFBW/NDShowVORDCapt",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cpt_ndb",
        "xplane_dref_address": "AirbusFBW/NDShowNDBCapt",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cpt_arpt",
        "xplane_dref_address": "AirbusFBW/NDShowARPTCapt",
    },
]
main_panel_buttons.extend(nd_show_buttons)


autopilot_buttons = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/spd_mach",
        "xplane_command_address": "sim/autopilot/knots_mach_toggle",
    },
    {"control_type": PushButton, "touchosc_address": "/button/appr", "xplane_command_address": "AirbusFBW/APPRbutton",},
    {
        "control_type": PushButton,
        "touchosc_address": "/button/a_thr",
        "xplane_command_address": "AirbusFBW/ATHRbutton",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/exped",
        "xplane_command_address": "AirbusFBW/EXPEDbutton",
    },
    {"control_type": PushButton, "touchosc_address": "/button/loc", "xplane_command_address": "AirbusFBW/LOCbutton",},
    {
        "control_type": PushButton,
        "touchosc_address": "/button/alt_pull",
        "xplane_command_address": "AirbusFBW/PullAltitude",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/hdg_trk_pull",
        "xplane_command_address": "AirbusFBW/PullHDGSel",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/spd_mach_pull",
        "xplane_command_address": "AirbusFBW/PullSPDSel",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/v_s_fpa_pull",
        "xplane_command_address": "AirbusFBW/PullVSSel",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/alt_push",
        "xplane_command_address": "AirbusFBW/PushAltitude",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/hdg_trk_push",
        "xplane_command_address": "AirbusFBW/PushHDGSel",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/spd_mach_push",
        "xplane_command_address": "AirbusFBW/PushSPDSel",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/v_s_fpa_push",
        "xplane_command_address": "AirbusFBW/PushVSSel",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/hdg_trk_v_s_fpa",
        "xplane_dref_address": "AirbusFBW/HDGTRKmode",
    },
]
main_panel_buttons.extend(autopilot_buttons)
