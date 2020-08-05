##########################################################################################
# MAIN PANEL BUTTONS
##########################################################################################

from lib.controls import PushButton
from aircraft.A319.controls import AirbusQNHStandardButton

main_panel_buttons = [
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
    # AirbusFBW/BaroStdCapt
    {
        "control_type": AirbusQNHStandardButton,
        "touchosc_address": "/button/cpt_qnh",
        "xplane_dref_address": "AirbusFBW/BaroStdCapt",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cpt_chrono",
        "xplane_command_address": "AirbusFBW/CaptChronoButton",
    },
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
    {
        "control_type": PushButton,
        "touchosc_address": "/button/spd_mach",
        "xplane_command_address": "sim/autopilot/knots_mach_toggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/appr",
        "xplane_command_address": "AirbusFBW/APPRbutton",
    },
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
    {
        "control_type": PushButton,
        "touchosc_address": "/button/loc",
        "xplane_command_address": "AirbusFBW/LOCbutton",
    },
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
        "xplane_command_address": "toliss_airbus/dispcommands/HeadingTrackModeSwitch",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/ap_1",
        "xplane_command_address": "toliss_airbus/ap1_push",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/ap_2",
        "xplane_command_address": "toliss_airbus/ap2_push",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cpt_ls",
        "xplane_command_address": "toliss_airbus/dispcommands/CaptLSButtonPush",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/metric_alt",
        "xplane_command_address": "toliss_airbus/dispcommands/MetricAltitudeSwitch",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cpt_terr_on_nd",
        "xplane_command_address": "toliss_airbus/dispcommands/TerrOnND1Toggle",
    },
    # Need to combine these two?
    # toliss_airbus/fd1_push
    # toliss_airbus/fd2_push
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cpt_fd",
        "xplane_command_address": "toliss_airbus/fd1_push",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/loc",
        "xplane_command_address": "toliss_airbus/loc_push",
    },
    # sim/instruments/timer_reset
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "sim/instruments/timer_reset",
    },
    # sim/instruments/timer_show_date
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "sim/instruments/timer_show_date",
    },
    # sim/instruments/timer_start_stop
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "sim/instruments/timer_start_stop",
    },
    # AirbusFBW/PFDNDToggleCapt[1] (will switch back to 0 after pressed)
]
