##########################################################################################
# OVERHEAD PANEL BUTTONS
##########################################################################################

from lib.controls import PushButton

overhead_panel_buttons = []

calls_buttons = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/calls_mech",
        "xplane_command_address": "AirbusFBW/purser/mech",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/calls_fwd",
        "xplane_command_address": "AirbusFBW/purser/fwd",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/calls_aft",
        "xplane_command_address": "AirbusFBW/purser/aft",
    },
]
overhead_panel_buttons.extend(calls_buttons)

# AirbusFBW/FuelOHPArray[32] // All values checked
fuel_pump_buttons = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_ltk_pumps_1",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_ltk_pumps_2",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_ctr_tk_1",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 2,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_ctr_tk_2",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 3,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_rtk_pumps_1",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 4,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_rtk_pumps_2",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 5,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_mode_sel",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 6,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_x_feed",
        "xplane_dref_address": "AirbusFBW/FuelOHPArray",
        "xplane_dref_index": 7,
    },
]
overhead_panel_buttons.extend(fuel_pump_buttons)

apu_buttons = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/apu_master_sw",
        "xplane_dref_address": "AirbusFBW/APUMaster",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/apu_start",
        "xplane_dref_address": "AirbusFBW/APUStarter",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/air_cond_apu_bleed",
        "xplane_dref_address": "AirbusFBW/APUBleedSwitch",
    },
]
overhead_panel_buttons.extend(apu_buttons)

# AirbusFBW/ElecOHPArray[32] // All values checked
ElecOHPArray = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_gen_1",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_gen_2",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_apu_gen",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 2,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_ext_pwr",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 3,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_bus_tie",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 4,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_bat_1",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 5,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_bat_2",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 6,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_ac_ess_feed",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 7,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_commercial",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 8,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_galley",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 9,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_gen_1_line",
        "xplane_dref_address": "AirbusFBW/ElecOHPArray",
        "xplane_dref_index": 13,
    },
]
overhead_panel_buttons.extend(ElecOHPArray)

apu_starter = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/apu_gen",
        "xplane_command_address": "AirbusFBW/APUStarter",
    },
]
overhead_panel_buttons.extend(apu_starter)

calls_emer_button = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/calls_emer",
        "xplane_dref_address": "AirbusFBW/EmerCallOHPButton",
    },
]
overhead_panel_buttons.extend(calls_emer_button)

# AirbusFBW/FireExOHPArray[16] // All values checked
fire_ex_ohp_array = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fire_apu_fire",
        "xplane_dref_address": "AirbusFBW/FireExOHPArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fire_apu_agent",
        "xplane_dref_address": "AirbusFBW/FireExOHPArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fire_eng_1_agent_1",
        "xplane_dref_address": "AirbusFBW/FireExOHPArray",
        "xplane_dref_index": 2,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fire_eng_1_agent_2",
        "xplane_dref_address": "AirbusFBW/FireExOHPArray",
        "xplane_dref_index": 3,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fire_eng_2_agent_1",
        "xplane_dref_address": "AirbusFBW/FireExOHPArray",
        "xplane_dref_index": 4,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fire_eng_2_agent_2",
        "xplane_dref_address": "AirbusFBW/FireExOHPArray",
        "xplane_dref_index": 5,
    },
]
overhead_panel_buttons.extend(fire_ex_ohp_array)

# AirbusFBW/HydOHPArray[24] // All values checked
hyd_ohp_array = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/hyd_eng_1_pump",
        "xplane_dref_address": "AirbusFBW/HydOHPArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/hyd_eng_2_pump",
        "xplane_dref_address": "AirbusFBW/HydOHPArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/hyd_blue_elec_pump",
        "xplane_dref_address": "AirbusFBW/HydOHPArray",
        "xplane_dref_index": 2,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/hyd_yellow_elec_pump",
        "xplane_dref_address": "AirbusFBW/HydOHPArray",
        "xplane_dref_index": 3,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/hyd_ptu",
        "xplane_dref_address": "AirbusFBW/HydOHPArray",
        "xplane_dref_index": 4,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/hyd_rat_man_on",
        "xplane_dref_address": "AirbusFBW/HydOHPArray",
        "xplane_dref_index": 5,
    },
]
overhead_panel_buttons.extend(hyd_ohp_array)

adr_buttons = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/adr1",
        "xplane_dref_address": "AirbusFBW/ADRSwitchArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/adr2",
        "xplane_dref_address": "AirbusFBW/ADRSwitchArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/adr3",
        "xplane_dref_address": "AirbusFBW/ADRSwitchArray",
        "xplane_dref_index": 2,
    },
]
overhead_panel_buttons.extend(adr_buttons)

# AirbusFBW/ENGFireSwitchArray[4] // All values checked
eng_fire_switch_array = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fire_eng_1_fire",
        "xplane_dref_address": "AirbusFBW/ENGFireSwitchArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fire_eng_2_fire",
        "xplane_dref_address": "AirbusFBW/ENGFireSwitchArray",
        "xplane_dref_index": 1,
    },
]
overhead_panel_buttons.extend(eng_fire_switch_array)

# AirbusFBW/FCCSwitchArray[16] // All values checked
fcc_switch_array = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/flt_ctl_elac_1",
        "xplane_dref_address": "AirbusFBW/FCCSwitchArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/flt_ctl_elac_2",
        "xplane_dref_address": "AirbusFBW/FCCSwitchArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/flt_ctl_sec_1",
        "xplane_dref_address": "AirbusFBW/FCCSwitchArray",
        "xplane_dref_index": 2,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/flt_ctl_sec_2",
        "xplane_dref_address": "AirbusFBW/FCCSwitchArray",
        "xplane_dref_index": 3,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/flt_ctl_sec_3",
        "xplane_dref_address": "AirbusFBW/FCCSwitchArray",
        "xplane_dref_index": 4,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/flt_ctl_fac_1",
        "xplane_dref_address": "AirbusFBW/FCCSwitchArray",
        "xplane_dref_index": 5,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/flt_ctl_fac_2",
        "xplane_dref_address": "AirbusFBW/FCCSwitchArray",
        "xplane_dref_index": 6,
    },
]
overhead_panel_buttons.extend(fcc_switch_array)

# AirbusFBW/GPWSSwitchArray[8] // All values checked
gpws_switch_array = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/gpws_sys",
        "xplane_dref_address": "AirbusFBW/GPWSSwitchArray",
        "xplane_dref_index": 0,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/gpws_g_s_mode",
        "xplane_dref_address": "AirbusFBW/GPWSSwitchArray",
        "xplane_dref_index": 1,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/gpws_flap_mode",
        "xplane_dref_address": "AirbusFBW/GPWSSwitchArray",
        "xplane_dref_index": 2,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/gpws_ldg_flap_3",
        "xplane_dref_address": "AirbusFBW/GPWSSwitchArray",
        "xplane_dref_index": 3,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/gpws_terr",
        "xplane_dref_address": "AirbusFBW/GPWSSwitchArray",
        "xplane_dref_index": 4,
    },
]
overhead_panel_buttons.extend(gpws_switch_array)


probe_window_heat_button = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/probe_window_heat",
        "xplane_dref_address": "AirbusFBW/ProbeHeatSwitch",
    },
]
overhead_panel_buttons.extend(probe_window_heat_button)

# AirbusFBW/FireTestAPU
# AirbusFBW/FireTestENG1
# AirbusFBW/FireTestENG2
