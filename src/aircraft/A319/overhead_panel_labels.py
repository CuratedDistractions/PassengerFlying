##########################################################################################
"""     OVERHEAD PANEL LABELS """
##########################################################################################

from aircraft.A319.controls import AirbusButtonLabel
from lib.controls import DynamicLabel
import logging

# Create a logger object.
logger = logging.getLogger(__name__)

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
ohp_lights_ata24 = set_xplane_dref_address_and_control_type(ohp_lights_ata24, "AirbusFBW/OHPLightsATA24")
overhead_panel_labels.extend(ohp_lights_ata24)


# AirbusFBW/OHPLightsATA26[64]
ohp_lights_ata26 = [
    {"xplane_dref_index": 0, "touchosc_address": "/label/fire_eng_1",},
    {"xplane_dref_index": 1, "touchosc_address": "/label/fire_eng_1_agent_1_lower",},
    {"xplane_dref_index": 2, "touchosc_address": "/label/fire_eng_1_agent_1_upper",},
    {"xplane_dref_index": 3, "touchosc_address": "/label/fire_eng_1_agent_2_lower",},
    {"xplane_dref_index": 4, "touchosc_address": "/label/fire_eng_1_agent_2_upper",},
    {"xplane_dref_index": 5, "touchosc_address": "/label/fire_eng_2",},
    {"xplane_dref_index": 6, "touchosc_address": "/label/fire_eng_2_agent_1_lower",},
    {"xplane_dref_index": 7, "touchosc_address": "/label/fire_eng_2_agent_1_upper",},
    {"xplane_dref_index": 8, "touchosc_address": "/label/fire_eng_2_agent_2_lower",},
    {"xplane_dref_index": 9, "touchosc_address": "/label/fire_eng_2_agent_2_lower",},
    # {"xplane_dref_index": 20, "touchosc_address": "/label/fire_"},
    # {"xplane_dref_index": 21, "touchosc_address": "/ovhd/label"},
    {"xplane_dref_index": 22, "touchosc_address": "/label/fire_apu_agent_lower",},
]
ohp_lights_ata26 = set_xplane_dref_address_and_control_type(ohp_lights_ata26, "AirbusFBW/OHPLightsATA26")
overhead_panel_labels.extend(ohp_lights_ata26)


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
ohp_lights_ata30 = set_xplane_dref_address_and_control_type(ohp_lights_ata30, "AirbusFBW/OHPLightsATA30")
overhead_panel_labels.extend(ohp_lights_ata30)


# AirbusFBW/OHPLightsATA31[64] (also defined in main_panel_labels and pedestal_labels)
ohp_lights_ata31 = [
    {"xplane_dref_index": 10, "touchosc_address": "/label/evac_command_lower"},
    {"xplane_dref_index": 11, "touchosc_address": "/label/evac_command_upper"},
    {"xplane_dref_index": 12, "touchosc_address": "/label/emer_exit_lt"},
    {"xplane_dref_index": 13, "touchosc_address": "/label/calls_emer_lower",},
    {"xplane_dref_index": 14, "touchosc_address": "/label/calls_emer_upper",},
    {"xplane_dref_index": 15, "touchosc_address": "/label/rcdr_gnd_ctl",},
]
ohp_lights_ata31 = set_xplane_dref_address_and_control_type(ohp_lights_ata31, "AirbusFBW/OHPLightsATA31")
overhead_panel_labels.extend(ohp_lights_ata31)


# AirbusFBW/OHPLightsATA34[64] (also defined in main_panel_labels)
ohp_lights_ata34 = [
    {"xplane_dref_index": 0, "touchosc_address": "/label/adr1_lower",},
    {"xplane_dref_index": 1, "touchosc_address": "/label/adr1_upper",},
    {"xplane_dref_index": 2, "touchosc_address": "/label/adr2_lower",},
    {"xplane_dref_index": 3, "touchosc_address": "/label/adr2_upper",},
    {"xplane_dref_index": 4, "touchosc_address": "/label/adr3_lower",},
    {"xplane_dref_index": 5, "touchosc_address": "/label/adr3_upper",},
    {"xplane_dref_index": 6, "touchosc_address": "/label/adirs_ir1_lower"},
    {"xplane_dref_index": 7, "touchosc_address": "/label/adirs_ir1_upper"},
    {"xplane_dref_index": 8, "touchosc_address": "/label/adirs_ir2_lower"},
    {"xplane_dref_index": 9, "touchosc_address": "/label/adirs_ir2_upper"},
    {"xplane_dref_index": 10, "touchosc_address": "/label/adirs_ir3_lower"},
    {"xplane_dref_index": 11, "touchosc_address": "/label/adirs_ir3_upper"},
    {"xplane_dref_index": 12, "touchosc_address": "/label/adirs_battery"},
    {"xplane_dref_index": 13, "touchosc_address": "/label/gpws_sys_lower",},
    {"xplane_dref_index": 14, "touchosc_address": "/label/gpws_sys_upper",},
    {"xplane_dref_index": 15, "touchosc_address": "/label/gpws_g_s_mode",},
    {"xplane_dref_index": 16, "touchosc_address": "/label/gpws_flap_mode",},
    {"xplane_dref_index": 17, "touchosc_address": "/label/gpws_ldg_flap_3",},
    # {"xplane_dref_index": 20, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    # {"xplane_dref_index": 21, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    # {"xplane_dref_index": 22, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    # {"xplane_dref_index": 23, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE"},
    {"xplane_dref_index": 26, "touchosc_address": "/label/gpws_terr_lower",},
    {"xplane_dref_index": 27, "touchosc_address": "/label/gpws_terr_upper",},
]
ohp_lights_ata34 = set_xplane_dref_address_and_control_type(ohp_lights_ata34, "AirbusFBW/OHPLightsATA34")
overhead_panel_labels.extend(ohp_lights_ata34)


# AirbusFBW/OHPLightsATA35[64]
ohp_lights_ata35 = [
    {"xplane_dref_index": 1, "touchosc_address": "/label/crew_supply",},
]
ohp_lights_ata35 = set_xplane_dref_address_and_control_type(ohp_lights_ata35, "AirbusFBW/OHPLightsATA35")
overhead_panel_labels.extend(ohp_lights_ata35)


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


# AirbusFBW/OHPLightsATA70[64]
ohp_lights_ata70 = [
    {"xplane_dref_index": 0, "touchosc_address": "/label/eng_man_start_1",},
    {"xplane_dref_index": 1, "touchosc_address": "/label/eng_man_start_2",},
]
ohp_lights_ata70 = set_xplane_dref_address_and_control_type(ohp_lights_ata70, "AirbusFBW/OHPLightsATA70")
overhead_panel_labels.extend(ohp_lights_ata70)


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
overhead_panel_labels.extend(battery_voltage_indicated_volts)
