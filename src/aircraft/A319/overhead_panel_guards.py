##########################################################################################
# OVERHEAD PANEL GUARDS
##########################################################################################

from lib.controls import PushButton

overhead_panel_guards = []

# AirbusFBW/OHPGuardsAllATA[64] //
ohp_guards_all_ata = [
    {
        "control_type": PushButton,
        "touchosc_address": "/button/emer_elec_pwr_man_on_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 0,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/hyd_blue_elec_pump_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 1,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/hyd_rat_man_on_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 2,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/air_cond_ram_air_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 3,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cabin_press_ditching_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 4,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_idg_1_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 5,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/elec_idg_2_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 6,
    },
    # Nr 7: I hear a sound, but I can't find any guard moving...
    # {
    #     "control_type": PushButton,
    #     "touchosc_address": "/button/",
    #     "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
    #     "xplane_dref_index": 7,
    # },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/emer_elec_pwp_emer_gen_test_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 8,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/oxygen_mask_man_on_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 9,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cargo_smoke_disch_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 11,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/cargo_smoke_ditch_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 12,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/eng_man_start_1_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 13,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/eng_man_start_2_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 14,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fire_eng_1_fire_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 17,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fire_eng_2_fire_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 18,
    },
    {
        "control_type": PushButton,
        "touchosc_address": "/button/fire_apu_fire_guard",
        "xplane_dref_address": "AirbusFBW/OHPGuardsAllATA",
        "xplane_dref_index": 19,
    },
]
overhead_panel_guards.extend(ohp_guards_all_ata)
