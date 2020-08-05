##########################################################################################
# OVERHEAD PANEL BUTTONS
##########################################################################################

from lib.controls import PushButton

overhead_panel_buttons = [
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
    # AirbusFBW/FuelOHPArray[32] // All values checked
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_ltk_pumps_1",
        "xplane_command_address": "toliss_airbus/fuelcommands/PumpLWing1Toggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_ltk_pumps_2",
        "xplane_command_address": "toliss_airbus/fuelcommands/PumpLWing2Toggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_ctr_tk_1",
        "xplane_command_address": "toliss_airbus/fuelcommands/PumpLCenterToggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_ctr_tk_2",
        "xplane_command_address": "toliss_airbus/fuelcommands/PumpRCenterToggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_rtk_pumps_1",
        "xplane_command_address": "toliss_airbus/fuelcommands/PumpRWing1Toggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fuel_rtk_pumps_2",
        "xplane_command_address": "toliss_airbus/fuelcommands/PumpRWing2Toggle",
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
    # APU
    {
        "control_type": PushButton,
        "touchosc_address": "/button/apu_master_sw",
        "xplane_command_address": "toliss_airbus/apucommands/MasterToggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/apu_start",
        "xplane_command_address": "toliss_airbus/apucommands/StarterToggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/air_cond_apu_bleed",
        "xplane_command_address": "toliss_airbus/apucommands/BleedToggle",
    },
    # AirbusFBW/ElecOHPArray[32] // All values checked
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
        "xplane_command_address": "toliss_airbus/eleccommands/ExtPowToggle",
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
        "xplane_command_address": "toliss_airbus/eleccommands/Bat1Toggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_bat_2",
        "xplane_command_address": "toliss_airbus/eleccommands/Bat2Toggle",
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
    {
        "control_type": PushButton,
        "touchosc_address": "/button/apu_gen",
        "xplane_command_address": "AirbusFBW/APUStarter",
    },
    # Calls
    {
        "control_type": PushButton,
        "touchosc_address": "/button/calls_emer",
        "xplane_dref_address": "AirbusFBW/EmerCallOHPButton",
    },
    # AirbusFBW/FireExOHPArray[16] // All values checked
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
    # AirbusFBW/HydOHPArray[24] // All values checked
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
    # ADR
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
    # AirbusFBW/ENGFireSwitchArray[4] // All values checked
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
    # AirbusFBW/FCCSwitchArray[16] // All values checked
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
    # AirbusFBW/GPWSSwitchArray[8] // All values checked
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
    # Probe window heat
    {
        "control_type": PushButton,
        "touchosc_address": "/button/probe_window_heat",
        "xplane_dref_address": "AirbusFBW/ProbeHeatSwitch",
    },
    # Fire test
    {
        "control_type": PushButton,
        "touchosc_address": "/NOT_DEFINED",
        "xplane_dref_address": "AirbusFBW/FireTestAPU",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/NOT_DEFINED",
        "xplane_dref_address": "AirbusFBW/FireTestENG1",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/NOT_DEFINED",
        "xplane_dref_address": "AirbusFBW/FireTestENG2",
    },
    # Packs
    {
        "control_type": PushButton,
        "touchosc_address": "/button/air_cond_pack_1",
        "xplane_command_address": "toliss_airbus/aircondcommands/Pack1Toggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/air_cond_pack_2",
        "xplane_command_address": "toliss_airbus/aircondcommands/Pack2Toggle",
    },
    # Anti Ice
    {
        "control_type": PushButton,
        "touchosc_address": "/button/anti_ice_wing",
        "xplane_command_address": "toliss_airbus/antiicecommands/WingToggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/anti_ice_eng_1",
        "xplane_command_address": "toliss_airbus/antiicecommands/ENG1Toggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/anti_ice_eng_2",
        "xplane_command_address": "toliss_airbus/antiicecommands/ENG2Toggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/NOT_DEFINED",
        "xplane_command_address": "toliss_airbus/gpwscommands/Flap3Toggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/NOT_DEFINED",
        "xplane_command_address": "toliss_airbus/gpwscommands/FlapModeToggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/NOT_DEFINED",
        "xplane_command_address": "toliss_airbus/gpwscommands/GSModeToggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/NOT_DEFINED",
        "xplane_command_address": "toliss_airbus/gpwscommands/SystemToggle",
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/NOT_DEFINED",
        "xplane_command_address": "toliss_airbus/gpwscommands/TerrainToggle",
    },
]
