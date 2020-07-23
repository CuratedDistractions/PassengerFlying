##########################################################################################
"""     OVERHEAD PANEL LABELS """
##########################################################################################

from aircraft.A319.controls import AirbusButtonLabel
from lib.controls import DynamicLabel

# Some constants for TouchOSC
RED = "red"
GREEN = "green"
BLUE = "blue"
YELLOW = "yellow"
PURPLE = "purple"
GRAY = "gray"
GREY = "gray"
ORANGE = "orange"
BROWN = "brown"
PINK = "pink"

overhead_panel_labels = []


def set_xplane_dref_address_and_control_type(item_list: list, xplane_dref_address=None):
    for idx, item in enumerate(item_list):
        item_list[idx]["xplane_dref_address"] = xplane_dref_address
        item_list[idx]["control_type"] = AirbusButtonLabel
    return item_list


# AirbusFBW/OHPLightsATA21[64]
ohp_lights_ata21 = [
    {"xplane_dref_index": 0, "touchosc_address": "/label/air_cond_eng_1_bleed_lower"},
    {"xplane_dref_index": 1, "touchosc_address": "/label/air_cond_eng_1_bleed_upper"},
    {"xplane_dref_index": 2, "touchosc_address": "/label/air_cond_eng_2_bleed_lower"},
    {"xplane_dref_index": 3, "touchosc_address": "/label/air_cond_eng_2_bleed_upper"},
    {"xplane_dref_index": 4, "touchosc_address": "/label/air_cond_apu_bleed_lower"},
    {"xplane_dref_index": 5, "touchosc_address": "/label/air_cond_apu_bleed_upper"},
    {"xplane_dref_index": 6, "touchosc_address": "/label/air_cond_pack_1_lower"},
    {"xplane_dref_index": 7, "touchosc_address": "/label/air_cond_pack_1_upper"},
    {"xplane_dref_index": 8, "touchosc_address": "/label/air_cond_pack_2_lower"},
    {"xplane_dref_index": 9, "touchosc_address": "/label/air_cond_pack_2_upper"},
    {"xplane_dref_index": 10, "touchosc_address": "/label/air_cond_hot_air_lower"},
    {"xplane_dref_index": 11, "touchosc_address": "/label/air_cond_hot_air_upper"},
    {"xplane_dref_index": 12, "touchosc_address": "/label/air_cond_ram_air"},
    {"xplane_dref_index": 13, "touchosc_address": "/label/cabin_press_ditching"},
    {"xplane_dref_index": 14, "touchosc_address": "/label/cabin_press_mode_sel"},
    # {"xplane_dref_index": 15, "touchosc_address": "/label/"},
    {"xplane_dref_index": 16, "touchosc_address": "/label/ventilation_cab_fans"},
    {"xplane_dref_index": 17, "touchosc_address": "/label/ventilation_extract_lower"},
    {"xplane_dref_index": 18, "touchosc_address": "/label/ventilation_extract_upper"},
    {"xplane_dref_index": 19, "touchosc_address": "/label/ventilation_blower_lower",},
    {"xplane_dref_index": 20, "touchosc_address": "/label/ventilation_blower_upper",},
    {"xplane_dref_index": 21, "touchosc_address": "/label/fwd_isol_valve_lower",},
    {"xplane_dref_index": 22, "touchosc_address": "/label/fwd_isol_valve_upper",},
    {"xplane_dref_index": 23, "touchosc_address": "/label/aft_isol_valve_lower",},
    {"xplane_dref_index": 24, "touchosc_address": "/label/aft_isol_valve_upper",},
    {"xplane_dref_index": 25, "touchosc_address": "/label/hot_air_lower",},
    {"xplane_dref_index": 26, "touchosc_address": "/label/hot_air_upper",},
]
# Add xplane_dref to this list
ohp_lights_ata21 = set_xplane_dref_address_and_control_type(ohp_lights_ata21, "AirbusFBW/OHPLightsATA21")
overhead_panel_labels.extend(ohp_lights_ata21)

# AirbusFBW/OHPLightsATA24[64]
ohp_lights_ata24 = [
    {"xplane_dref_index": 0, "touchosc_address": "/label/elec_gen_1_lower",},
    {"xplane_dref_index": 1, "touchosc_address": "/label/elec_gen_1_upper",},
    {"xplane_dref_index": 2, "touchosc_address": "/label/elec_gen_2_lower",},
    {"xplane_dref_index": 3, "touchosc_address": "/label/elec_gen_2_upper",},
    {"xplane_dref_index": 4, "touchosc_address": "/label/elec_apu_gen_lower"},
    {"xplane_dref_index": 5, "touchosc_address": "/label/elec_apu_gen_upper"},
    {"xplane_dref_index": 6, "touchosc_address": "/label/elec_ext_pwr_lower"},
    {"xplane_dref_index": 7, "touchosc_address": "/label/elec_ext_pwr_upper"},
    {"xplane_dref_index": 8, "touchosc_address": "/label/elec_bus_tie",},
    {"xplane_dref_index": 9, "touchosc_address": "/label/elec_bat_1_lower"},
    {"xplane_dref_index": 10, "touchosc_address": "/label/elec_bat_1_upper"},
    {"xplane_dref_index": 11, "touchosc_address": "/label/elec_bat_2_lower"},
    {"xplane_dref_index": 12, "touchosc_address": "/label/elec_bat_2_upper"},
    {"xplane_dref_index": 13, "touchosc_address": "/label/elec_ac_ess_feed_lower",},
    {"xplane_dref_index": 14, "touchosc_address": "/label/elec_ac_ess_feed_upper",},
    {"xplane_dref_index": 15, "touchosc_address": "/label/elec_commercial"},
    {"xplane_dref_index": 16, "touchosc_address": "/label/elec_galley_lower",},
    {"xplane_dref_index": 17, "touchosc_address": "/label/elec_galley_upper",},
    # {"xplane_dref_index": 18, "touchosc_address": "/ovhd/label"},
    # {"xplane_dref_index": 19, "touchosc_address": "/ovhd/label"},
    # {"xplane_dref_index": 20, "touchosc_address": "/ovhd/label"},
    {"xplane_dref_index": 21, "touchosc_address": "/label/emer_elec_pwr_gen_1_line_lower",},
    {"xplane_dref_index": 22, "touchosc_address": "/label/emer_elec_pwr_gen_1_line_upper",},
]
# Add xplane_dref to this list
ohp_lights_ata24 = set_xplane_dref_address_and_control_type(ohp_lights_ata24, "AirbusFBW/OHPLightsATA24")
overhead_panel_labels.extend(ohp_lights_ata24)


# AirbusFBW/OHPLightsATA27[64]
ohp_lights_ata27 = [
    {"xplane_dref_index": 0, "touchosc_address": "/label/flt_ctl_elac_1_lower",},
    {"xplane_dref_index": 1, "touchosc_address": "/label/flt_ctl_elac_1_upper",},
    {"xplane_dref_index": 2, "touchosc_address": "/label/flt_ctl_elac_2_lower",},
    {"xplane_dref_index": 3, "touchosc_address": "/label/flt_ctl_elac_2_upper",},
    {"xplane_dref_index": 4, "touchosc_address": "/label/flt_ctl_sec_1_lower",},
    {"xplane_dref_index": 5, "touchosc_address": "/label/flt_ctl_sec_1_upper",},
    {"xplane_dref_index": 6, "touchosc_address": "/label/flt_ctl_sec_2_lower",},
    {"xplane_dref_index": 7, "touchosc_address": "/label/flt_ctl_sec_2_upper",},
    {"xplane_dref_index": 8, "touchosc_address": "/label/flt_ctl_sec_3_lower",},
    {"xplane_dref_index": 9, "touchosc_address": "/label/flt_ctl_sec_3_upper",},
    {"xplane_dref_index": 10, "touchosc_address": "/label/flt_ctl_fac_1_lower",},
    {"xplane_dref_index": 11, "touchosc_address": "/label/flt_ctl_fac_1_upper",},
    {"xplane_dref_index": 12, "touchosc_address": "/label/flt_ctl_fac_2_lower",},
    {"xplane_dref_index": 13, "touchosc_address": "/label/flt_ctl_fac_2_upper",},
]
# Add xplane_dref to this list
ohp_lights_ata27 = set_xplane_dref_address_and_control_type(ohp_lights_ata27, "AirbusFBW/OHPLightsATA27")
overhead_panel_labels.extend(ohp_lights_ata27)

# AirbusFBW/OHPLightsATA28[64]
ohp_lights_ata28 = [
    {"xplane_dref_index": 0, "touchosc_address": "/label/fuel_ltk_pumps_1_lower"},
    {"xplane_dref_index": 1, "touchosc_address": "/label/fuel_ltk_pumps_1_upper"},
    {"xplane_dref_index": 2, "touchosc_address": "/label/fuel_ltk_pumps_2_lower"},
    {"xplane_dref_index": 3, "touchosc_address": "/label/fuel_ltk_pumps_2_upper"},
    {"xplane_dref_index": 4, "touchosc_address": "/label/fuel_ctr_tk_1_lower"},
    {"xplane_dref_index": 5, "touchosc_address": "/label/fuel_ctr_tk_1_upper"},
    {"xplane_dref_index": 6, "touchosc_address": "/label/fuel_ctr_tk_2_lower"},
    {"xplane_dref_index": 7, "touchosc_address": "/label/fuel_ctr_tk_2_upper"},
    {"xplane_dref_index": 8, "touchosc_address": "/label/fuel_rtk_pumps_1_lower"},
    {"xplane_dref_index": 9, "touchosc_address": "/label/fuel_rtk_pumps_1_upper"},
    {"xplane_dref_index": 10, "touchosc_address": "/label/fuel_rtk_pumps_2_lower"},
    {"xplane_dref_index": 11, "touchosc_address": "/label/fuel_rtk_pumps_2_upper"},
    {"xplane_dref_index": 12, "touchosc_address": "/label/fuel_mode_sel_lower",},
    {"xplane_dref_index": 13, "touchosc_address": "/label/fuel_mode_sel_upper",},
    {"xplane_dref_index": 14, "touchosc_address": "/label/fuel_x_feed_lower",},
    {"xplane_dref_index": 15, "touchosc_address": "/label/fuel_x_feed_upper",},
]
# Add xplane_dref to this list
ohp_lights_ata28 = set_xplane_dref_address_and_control_type(ohp_lights_ata28, "AirbusFBW/OHPLightsATA28")
overhead_panel_labels.extend(ohp_lights_ata28)

# AirbusFBW/OHPLightsATA29[64]
ohp_lights_ata29 = [
    {"xplane_dref_index": 0, "touchosc_address": "/label/hyd_eng_1_pump_lower",},
    {"xplane_dref_index": 1, "touchosc_address": "/label/hyd_eng_1_pump_upper",},
    {"xplane_dref_index": 2, "touchosc_address": "/label/hyd_eng_2_pump_lower",},
    {"xplane_dref_index": 3, "touchosc_address": "/label/hyd_eng_2_pump_upper",},
    {"xplane_dref_index": 4, "touchosc_address": "/label/hyd_blue_elec_pump_lower",},
    {"xplane_dref_index": 5, "touchosc_address": "/label/hyd_blue_elec_pump_upper",},
    {"xplane_dref_index": 6, "touchosc_address": "/label/hyd_yellow_elec_pump_lower",},
    {"xplane_dref_index": 7, "touchosc_address": "/label/hyd_yellow_elec_pump_upper",},
    {"xplane_dref_index": 8, "touchosc_address": "/label/hyd_ptu_lower",},
    {"xplane_dref_index": 9, "touchosc_address": "/label/hyd_ptu_upper",},
]
# Add xplane_dref to this list
ohp_lights_ata29 = set_xplane_dref_address_and_control_type(ohp_lights_ata29, "AirbusFBW/OHPLightsATA29")
overhead_panel_labels.extend(ohp_lights_ata29)

# AirbusFBW/OHPLightsATA30[64]
ohp_lights_ata30 = [
    {"xplane_dref_index": 0, "touchosc_address": "/label/anti_ice_wing_lower"},
    {"xplane_dref_index": 1, "touchosc_address": "/label/anti_ice_wing_upper"},
    {"xplane_dref_index": 2, "touchosc_address": "/label/anti_ice_eng_1_lower"},
    {"xplane_dref_index": 3, "touchosc_address": "/label/anti_ice_eng_1_upper"},
    {"xplane_dref_index": 4, "touchosc_address": "/label/anti_ice_eng_2_lower"},
    {"xplane_dref_index": 5, "touchosc_address": "/label/anti_ice_eng_2_upper"},
    {"xplane_dref_index": 10, "touchosc_address": "/label/probe_window_heat"},
]
# Add xplane_dref to this list
ohp_lights_ata30 = set_xplane_dref_address_and_control_type(ohp_lights_ata30, "AirbusFBW/OHPLightsATA30")
overhead_panel_labels.extend(ohp_lights_ata30)

# AirbusFBW/OHPLightsATA31[64]
ohp_lights_ata31 = [
    # {"xplane_dref_index": 8, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    # {"xplane_dref_index": 9, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    # {"xplane_dref_index": 10, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "EVAC/ON", "remarks": "COMMAND"},
    # {"xplane_dref_index": 11, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "EVAC/ON", "remarks": "COMMAND"},
    {"xplane_dref_index": 12, "touchosc_address": "/label/emer_exit_lt"},
    {
        "xplane_dref_index": 13,
        "touchosc_address": "/ovhd/label543",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": GREY,
        # "remarks": "EMER",
    },
    {
        "xplane_dref_index": 14,
        "touchosc_address": "/ovhd/label544",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        # "remarks": "EMER",
    },
    # {
    #     "xplane_dref_index": 15,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "ON",
    #     "touchosc_initial_color": BLUE,
    #     "remarks": "GND CTL",
    # },
    # {
    #     "xplane_dref_index": 16,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - CSTR",
    # },
    # {
    #     "xplane_dref_index": 17,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - WPT",
    # },
    # {
    #     "xplane_dref_index": 18,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - VOR,D",
    # },
    # {
    #     "xplane_dref_index": 19,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - NDB",
    # },
    # {
    #     "xplane_dref_index": 20,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - ARPT",
    # },
    # {
    #     "xplane_dref_index": 21,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - ARPT",
    # },
    # {
    #     "xplane_dref_index": 22,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - NDB",
    # },
    # {
    #     "xplane_dref_index": 23,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - VOR,D",
    # },
    # {
    #     "xplane_dref_index": 24,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - WPT",
    # },
    # {
    #     "xplane_dref_index": 25,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - CSTR",
    # },
    # {
    #     "xplane_dref_index": 26,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - FD",
    # },
    # {
    #     "xplane_dref_index": 27,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - FD",
    # },
    # {
    #     "xplane_dref_index": 28,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - LS",
    # },
    # {
    #     "xplane_dref_index": 29,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - LS",
    # },
    # {
    #     "xplane_dref_index": 30,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "ENG",
    # },
    # {
    #     "xplane_dref_index": 31,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "BLEED",
    # },
    # {
    #     "xplane_dref_index": 32,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "PRESS",
    # },
    # {
    #     "xplane_dref_index": 33,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "ELEC",
    # },
    # {
    #     "xplane_dref_index": 34,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "HYD",
    # },
    # {
    #     "xplane_dref_index": 35,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FUEL",
    # },
    # {
    #     "xplane_dref_index": 36,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "APU",
    # },
    # {
    #     "xplane_dref_index": 37,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "COND",
    # },
    # {
    #     "xplane_dref_index": 38,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "DOOR",
    # },
    # {
    #     "xplane_dref_index": 39,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "WHEEL",
    # },
    # {
    #     "xplane_dref_index": 40,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "F/CTL",
    # },
    # {
    #     "xplane_dref_index": 41,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "STS",
    # },
    # {
    #     "xplane_dref_index": 42,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CLR (left)",
    # },
    # {
    #     "xplane_dref_index": 43,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CLR (right)",
    # },
    # {
    #     "xplane_dref_index": 44,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "AP 1",
    # },
    # {
    #     "xplane_dref_index": 45,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "AP 2",
    # },
    # {"xplane_dref_index": 46, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    # {"xplane_dref_index": 47, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    # {
    #     "xplane_dref_index": 48,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "APPR",
    # },
    # {"xplane_dref_index": 49, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    # {"xplane_dref_index": 50, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
]
# Add xplane_dref to this list
ohp_lights_ata31 = set_xplane_dref_address_and_control_type(ohp_lights_ata31, "AirbusFBW/OHPLightsATA31")
overhead_panel_labels.extend(ohp_lights_ata31)


# AirbusFBW/OHPLightsATA34[64]
ohp_lights_ata34 = [
    {
        "xplane_dref_index": 0,
        "touchosc_address": "/ovhd/label237",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        # "remarks": "ADR1",
    },
    {
        "xplane_dref_index": 1,
        "touchosc_address": "/ovhd/label238",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        # "remarks": "ADR1",
    },
    {
        "xplane_dref_index": 2,
        "touchosc_address": "/ovhd/label239",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        # "remarks": "ADR2",
    },
    {
        "xplane_dref_index": 3,
        "touchosc_address": "/ovhd/label240",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        # "remarks": "ADR2",
    },
    {
        "xplane_dref_index": 4,
        "touchosc_address": "/ovhd/label241",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        # "remarks": "ADR3",
    },
    {
        "xplane_dref_index": 5,
        "touchosc_address": "/ovhd/label242",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        # "remarks": "ADR3",
    },
    {"xplane_dref_index": 6, "touchosc_address": "/label/adirs_ir1_lower"},
    {"xplane_dref_index": 7, "touchosc_address": "/label/adirs_ir1_upper"},
    {"xplane_dref_index": 8, "touchosc_address": "/label/adirs_ir2_lower"},
    {"xplane_dref_index": 9, "touchosc_address": "/label/adirs_ir2_upper"},
    {"xplane_dref_index": 10, "touchosc_address": "/label/adirs_ir3_lower"},
    {"xplane_dref_index": 11, "touchosc_address": "/label/adirs_ir3_upper"},
    {"xplane_dref_index": 12, "touchosc_address": "/label/adirs_battery"},
    {
        "xplane_dref_index": 13,
        "touchosc_address": "/ovhd/label211",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        # "remarks": "GPWS - SYS",
    },
    {
        "xplane_dref_index": 14,
        "touchosc_address": "/ovhd/label212",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        # "remarks": "GPWS - SYS",
    },
    {
        "xplane_dref_index": 15,
        "touchosc_address": "/ovhd/label213",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        # "remarks": "G/S MODE",
    },
    {
        "xplane_dref_index": 16,
        "touchosc_address": "/ovhd/label215",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        # "remarks": "FLAP MODE",
    },
    {
        "xplane_dref_index": 17,
        "touchosc_address": "/ovhd/label217",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": GREY,
        # "remarks": "LDG FLAP 3",
    },
    # {"xplane_dref_index": 20, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    # {"xplane_dref_index": 21, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    # {"xplane_dref_index": 22, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    # {"xplane_dref_index": 23, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    # {
    #     "xplane_dref_index": 24,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "ON",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - TERR ON ND",
    # },
    # {
    #     "xplane_dref_index": 25,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "ON",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - TERR ON ND",
    # },
    {
        "xplane_dref_index": 26,
        "touchosc_address": "/ovhd/label209",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        # "remarks": "GPWS - TERR",
    },
    {
        "xplane_dref_index": 27,
        "touchosc_address": "/ovhd/label210",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        # "remarks": "GPWS - TERR",
    },
]
# Add xplane_dref to this list
ohp_lights_ata34 = set_xplane_dref_address_and_control_type(ohp_lights_ata34, "AirbusFBW/OHPLightsATA34")
overhead_panel_labels.extend(ohp_lights_ata34)

# AirbusFBW/OHPLightsATA49[64]
ohp_lights_ata49 = [
    {"xplane_dref_index": 0, "touchosc_address": "/label/apu_master_sw_lower"},
    {"xplane_dref_index": 1, "touchosc_address": "/label/apu_master_sw_upper"},
    {"xplane_dref_index": 2, "touchosc_address": "/label/apu_start_lower"},
    {"xplane_dref_index": 3, "touchosc_address": "/label/apu_start_upper"},
]
# Add xplane_dref to this list
ohp_lights_ata49 = set_xplane_dref_address_and_control_type(ohp_lights_ata49, "AirbusFBW/OHPLightsATA49")
overhead_panel_labels.extend(ohp_lights_ata49)

# AirbusFBW/BatVolts
battery_voltage_indicated_volts = [
    {
        "control_type": DynamicLabel,
        "xplane_dref_address": "AirbusFBW/BatVolts",
        "xplane_dref_index": 0,
        "touchosc_address": "/label/elec_battery_voltage_1",
    },
    {
        "control_type": DynamicLabel,
        "xplane_dref_address": "AirbusFBW/BatVolts",
        "xplane_dref_index": 1,
        "touchosc_address": "/label/elec_battery_voltage_2",
    },
]
# Add xplane_dref to this list
overhead_panel_labels.extend(battery_voltage_indicated_volts)
