##########################################################################################
# MAIN PANEL LABELS
##########################################################################################

from aircraft.A319.controls import AirbusLabel, AirbusQNHLabel
from lib.controls import MasterWarningButtonLabel, MasterCautionButtonLabel

main_panel_labels = [
    {
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 0,
        "touchosc_address": "/label/cpt_master_warning_lower",
        "control_type": MasterWarningButtonLabel,
    },
    {
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 0,
        "touchosc_address": "/label/cpt_master_warning_outline",
        "control_type": MasterWarningButtonLabel,
    },
    {
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 1,
        "touchosc_address": "/label/cpt_master_warning_upper",
        "control_type": MasterWarningButtonLabel,
    },
    {
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 2,
        "touchosc_address": "/label/fo_master_warning_lower",
        "control_type": MasterWarningButtonLabel,
    },
    {
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 3,
        "touchosc_address": "/label/fo_master_warning_upper",
        "control_type": MasterWarningButtonLabel,
    },
    {
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 4,
        "touchosc_address": "/label/cpt_master_caution_lower",
        "control_type": MasterCautionButtonLabel,
    },
    {
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 4,
        "touchosc_address": "/label/cpt_master_caution_outline",
        "control_type": MasterCautionButtonLabel,
    },
    {
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 5,
        "touchosc_address": "/label/cpt_master_caution_upper",
        "control_type": MasterCautionButtonLabel,
    },
    {
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 6,
        "touchosc_address": "/label/fo_master_caution_lower",
        "control_type": MasterCautionButtonLabel,
    },
    {
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 7,
        "touchosc_address": "/label/fo_master_caution_upper",
        "control_type": MasterCautionButtonLabel,
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 16,
        "touchosc_address": "/label/cpt_cstr",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 17,
        "touchosc_address": "/label/cpt_wpt",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 18,
        "touchosc_address": "/label/cpt_vor_d",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 19,
        "touchosc_address": "/label/cpt_ndb",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 20,
        "touchosc_address": "/label/cpt_arpt",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 21,
        "touchosc_address": "/label/fo_arpt",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 22,
        "touchosc_address": "/label/fo_ndb",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 23,
        "touchosc_address": "/label/fo_vor_d",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 24,
        "touchosc_address": "/label/fo_wpt",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 25,
        "touchosc_address": "/label/fo_cstr",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 26,
        "touchosc_address": "/label/cpt_fd",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 27,
        "touchosc_address": "/label/fo_fd",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 28,
        "touchosc_address": "/label/cpt_ls",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 29,
        "touchosc_address": "/label/fo_ls",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 44,
        "touchosc_address": "/label/ap_1",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 45,
        "touchosc_address": "/label/ap_2",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA31",
        "xplane_dref_index": 48,
        "touchosc_address": "/label/appr",
    },
    # AirbusFBW/OHPLightsATA32
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 0,
        "touchosc_address": "/label/ldg_gear_left_lower",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 1,
        "touchosc_address": "/label/ldg_gear_left_upper",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 2,
        "touchosc_address": "/label/ldg_gear_center_lower",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 3,
        "touchosc_address": "/label/ldg_gear_center_upper",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 4,
        "touchosc_address": "/label/ldg_gear_right_lower",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 5,
        "touchosc_address": "/label/ldg_gear_right_upper",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 10,
        "touchosc_address": "/label/brk_fan_lower",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 11,
        "touchosc_address": "/label/brk_fan_upper",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 12,
        "touchosc_address": "/label/auto_brk_lo_lower",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 13,
        "touchosc_address": "/label/auto_brk_lo_upper",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 14,
        "touchosc_address": "/label/auto_brk_med_lower",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 15,
        "touchosc_address": "/label/auto_brk_med_upper",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 16,
        "touchosc_address": "/label/auto_brk_max_lower",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA32",
        "xplane_dref_index": 17,
        "touchosc_address": "/label/auto_brk_max_upper",
    },
    # AirbusFBW/OHPLightsATA34[64] (also defined in overhead_panel_labels)
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA34",
        "xplane_dref_index": 24,
        "touchosc_address": "/labels/cpt_terr_on_nd",
    },
    {
        "control_type": AirbusLabel,
        "xplane_dref_address": "AirbusFBW/OHPLightsATA34",
        "xplane_dref_index": 25,
        "touchosc_address": "/labels/fo_terr_on_nd",
    },
    # AirbusFBW/ISIBaroSetting
    {
        "control_type": AirbusQNHLabel,
        "xplane_dref_address": "AirbusFBW/ISIBaroSetting",
        "touchosc_address": "/label/cpt_qnh",
    },
    # sim/cockpit2/autopilot/altitude_dial_ft[1]
    # sim/cockpit2/autopilot/airspeed_dial_kts[1]
    # sim/cockpit2/autopilot/airspeed_dial_kts_mach[1] (Shows the same value as just kts)
    # sim/cockpit2/autopilot/airspeed_is_mach[1]
    # sim/cockpit2/autopilot/vvi_dial_fpm[1]
    # sim/cockpit2/autopilot/heading_dial_deg_mag_pilot[1]
    # sim/cockpit2/autopilot/flight_director_pitch_deg[1]
    # sim/cockpit2/autopilot/flight_director_roll_deg[1]
]
