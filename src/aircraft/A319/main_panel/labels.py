##########################################################################################
# MAIN PANEL LABELS
##########################################################################################

from aircraft.A319.controls import AirbusLabel, AirbusQNHLabel
from lib.controls import MasterWarningButtonLabel, MasterCautionButtonLabel

main_panel_labels = []


def set_xplane_dref_address_and_control_type(item_list: list, xplane_dref_address=None):
    for idx, item in enumerate(item_list):
        item_list[idx]["xplane_dref_address"] = xplane_dref_address
        if "control_type" not in item_list[idx]:
            item_list[idx]["control_type"] = AirbusLabel
    return item_list


# AirbusFBW/OHPLightsATA31[64] (also defined in overhead_panel_labels and pedestal_labels)
ohp_lights_ata31 = [
    {
        "xplane_dref_index": 0,
        "touchosc_address": "/label/cpt_master_warning_lower",
        "control_type": MasterWarningButtonLabel,
    },
    {
        "xplane_dref_index": 0,
        "touchosc_address": "/label/cpt_master_warning_outline",
        "control_type": MasterWarningButtonLabel,
    },
    {
        "xplane_dref_index": 1,
        "touchosc_address": "/label/cpt_master_warning_upper",
        "control_type": MasterWarningButtonLabel,
    },
    {
        "xplane_dref_index": 2,
        "touchosc_address": "/label/fo_master_warning_lower",
        "control_type": MasterWarningButtonLabel,
    },
    {
        "xplane_dref_index": 3,
        "touchosc_address": "/label/fo_master_warning_upper",
        "control_type": MasterWarningButtonLabel,
    },
    {
        "xplane_dref_index": 4,
        "touchosc_address": "/label/cpt_master_caution_lower",
        "control_type": MasterCautionButtonLabel,
    },
    {
        "xplane_dref_index": 4,
        "touchosc_address": "/label/cpt_master_caution_outline",
        "control_type": MasterCautionButtonLabel,
    },
    {
        "xplane_dref_index": 5,
        "touchosc_address": "/label/cpt_master_caution_upper",
        "control_type": MasterCautionButtonLabel,
    },
    {
        "xplane_dref_index": 6,
        "touchosc_address": "/label/fo_master_caution_lower",
        "control_type": MasterCautionButtonLabel,
    },
    {
        "xplane_dref_index": 7,
        "touchosc_address": "/label/fo_master_caution_upper",
        "control_type": MasterCautionButtonLabel,
    },
    {"xplane_dref_index": 16, "touchosc_address": "/label/cpt_cstr",},
    {"xplane_dref_index": 17, "touchosc_address": "/label/cpt_wpt",},
    {"xplane_dref_index": 18, "touchosc_address": "/label/cpt_vor_d",},
    {"xplane_dref_index": 19, "touchosc_address": "/label/cpt_ndb",},
    {"xplane_dref_index": 20, "touchosc_address": "/label/cpt_arpt",},
    {"xplane_dref_index": 21, "touchosc_address": "/label/fo_arpt",},
    {"xplane_dref_index": 22, "touchosc_address": "/label/fo_ndb",},
    {"xplane_dref_index": 23, "touchosc_address": "/label/fo_vor_d",},
    {"xplane_dref_index": 24, "touchosc_address": "/label/fo_wpt",},
    {"xplane_dref_index": 25, "touchosc_address": "/label/fo_cstr",},
    {"xplane_dref_index": 26, "touchosc_address": "/label/cpt_fd",},
    {"xplane_dref_index": 27, "touchosc_address": "/label/fo_fd",},
    {"xplane_dref_index": 28, "touchosc_address": "/label/cpt_ls",},
    {"xplane_dref_index": 29, "touchosc_address": "/label/fo_ls",},
    {"xplane_dref_index": 44, "touchosc_address": "/label/ap_1",},
    {"xplane_dref_index": 45, "touchosc_address": "/label/ap_2",},
    # {"xplane_dref_index": 46, "touchosc_address": "/label/"},
    # {"xplane_dref_index": 47, "touchosc_address": "/label/"},
    {"xplane_dref_index": 48, "touchosc_address": "/label/appr",},
]
ohp_lights_ata31 = set_xplane_dref_address_and_control_type(ohp_lights_ata31, "AirbusFBW/OHPLightsATA31")
main_panel_labels.extend(ohp_lights_ata31)

# AirbusFBW/OHPLightsATA32
ohp_lights_ata32 = [
    {"xplane_dref_index": 0, "touchosc_address": "/label/ldg_gear_left_lower",},
    {"xplane_dref_index": 1, "touchosc_address": "/label/ldg_gear_left_upper",},
    {"xplane_dref_index": 2, "touchosc_address": "/label/ldg_gear_center_lower",},
    {"xplane_dref_index": 3, "touchosc_address": "/label/ldg_gear_center_upper",},
    {"xplane_dref_index": 4, "touchosc_address": "/label/ldg_gear_right_lower",},
    {"xplane_dref_index": 5, "touchosc_address": "/label/ldg_gear_right_upper",},
    {"xplane_dref_index": 10, "touchosc_address": "/label/brk_fan_lower",},
    {"xplane_dref_index": 11, "touchosc_address": "/label/brk_fan_upper"},
    {"xplane_dref_index": 12, "touchosc_address": "/label/auto_brk_lo_lower",},
    {"xplane_dref_index": 13, "touchosc_address": "/label/auto_brk_lo_upper"},
    {"xplane_dref_index": 14, "touchosc_address": "/label/auto_brk_med_lower",},
    {"xplane_dref_index": 15, "touchosc_address": "/label/auto_brk_med_upper"},
    {"xplane_dref_index": 16, "touchosc_address": "/label/auto_brk_max_lower",},
    {"xplane_dref_index": 17, "touchosc_address": "/label/auto_brk_max_upper",},
]
ohp_lights_ata32 = set_xplane_dref_address_and_control_type(ohp_lights_ata32, "AirbusFBW/OHPLightsATA32")
main_panel_labels.extend(ohp_lights_ata32)

# AirbusFBW/OHPLightsATA34[64] (also defined in overhead_panel_labels)
ohp_lights_ata34 = [
    {"xplane_dref_index": 24, "touchosc_address": "/labels/cpt_terr_on_nd",},
    {"xplane_dref_index": 25, "touchosc_address": "/labels/fo_terr_on_nd",},
]
ohp_lights_ata34 = set_xplane_dref_address_and_control_type(ohp_lights_ata34, "AirbusFBW/OHPLightsATA34")
main_panel_labels.extend(ohp_lights_ata34)


# AirbusFBW/ISIBaroSetting
isi_baro_setting = [
    {
        "control_type": AirbusQNHLabel,
        "xplane_dref_address": "AirbusFBW/ISIBaroSetting",
        "touchosc_address": "/label/cpt_qnh",
    },
]
main_panel_labels.extend(isi_baro_setting)

