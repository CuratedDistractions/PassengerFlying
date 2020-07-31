##########################################################################################
# PEDESTAL BUTTONS
##########################################################################################

from lib.controls import PushButton

pedestal_buttons = [
    # Transponder
    # AirbusFBW/ATCCodeKey0
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/ATCCodeKey0",},
    # AirbusFBW/ATCCodeKey1
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/ATCCodeKey1",},
    # AirbusFBW/ATCCodeKey2
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/ATCCodeKey2",},
    # AirbusFBW/ATCCodeKey3
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/ATCCodeKey3",},
    # AirbusFBW/ATCCodeKey4
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/ATCCodeKey4",},
    # AirbusFBW/ATCCodeKey5
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/ATCCodeKey5",},
    # AirbusFBW/ATCCodeKey6
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/ATCCodeKey6",},
    # AirbusFBW/ATCCodeKey7
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/ATCCodeKey7",},
    # AirbusFBW/ATCCodeKeyCLR
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "AirbusFBW/ATCCodeKeyCLR",
    },
    # sim/transponder/transponder_ident
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "sim/transponder/transponder_ident",
    },
    # ECAM
    # AirbusFBW/ECAMAll
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/ECAMAll",},
    # AirbusFBW/TOConfigPres
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/TOConfigPres",},
    # sim/annunciator/clear_master_accept
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "sim/annunciator/clear_master_accept",
    },
    # AirbusFBW/ECAMRecall
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/ECAMRecall",},
    # AirbusFBW/SDENG[1]
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/SDENG",},
    # AirbusFBW/SDBLEED[1]
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/SDBLEED",},
    # AirbusFBW/SDPRESS[1]
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/SDPRESS",},
    # AirbusFBW/SDELEC[1]
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/SDELEC",},
    # AirbusFBW/SDHYD[1]
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/SDHYD",},
    # AirbusFBW/SDFUEL[1]
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/SDFUEL",},
    # AirbusFBW/SDAPU[1]
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/SDAPU",},
    # AirbusFBW/SDCOND[1]
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/SDCOND",},
    # AirbusFBW/SDDOOR[1]
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/SDDOOR",},
    # AirbusFBW/SDWHEEL[1]
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/SDWHEEL",},
    # AirbusFBW/SDFCTL[1]
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/SDFCTL",},
    # AirbusFBW/SDSTATUS[1]
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/SDSTATUS",},
    # COM 1
    # AirbusFBW/ListenVHF1
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/ListenVHF1",},
    # AirbusFBW/ListenVHF2
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/ListenVHF2",},
    # AirbusFBW/RMP1FreqDownLrg
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "AirbusFBW/RMP1FreqDownLrg",
    },
    # AirbusFBW/RMP1FreqDownSml
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "AirbusFBW/RMP1FreqDownSml",
    },
    # AirbusFBW/RMP1FreqUpLrg
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "AirbusFBW/RMP1FreqUpLrg",
    },
    # AirbusFBW/RMP1FreqUpSml
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "AirbusFBW/RMP1FreqUpSml",
    },
    # AirbusFBW/RMPSwapCapt
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/RMPSwapCapt",},
    # AirbusFBW/VHF1Capt
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/VHF1Capt",},
    # AirbusFBW/VHF2Capt
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/VHF2Capt",},
    # COM 2
    # AirbusFBW/RMP2FreqDownLrg
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "AirbusFBW/RMP2FreqDownLrg",
    },
    # AirbusFBW/RMP2FreqDownSml
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "AirbusFBW/RMP2FreqDownSml",
    },
    # AirbusFBW/RMP2FreqUpLrg
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "AirbusFBW/RMP2FreqUpLrg",
    },
    # AirbusFBW/RMP2FreqUpSml
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "AirbusFBW/RMP2FreqUpSml",
    },
    # AirbusFBW/RMPSwapCo
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_command_address": "AirbusFBW/RMPSwapCo",},
    # AirbusFBW/ParkBrake[1] or toliss_airbus/park_brake_toggle
    {"control_type": PushButton, "touchosc_address": "/UNDEFINED", "xplane_dref_address": "AirbusFBW/ParkBrake",},
    # Trim
    # sim/flight_controls/pitch_trim_up
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "sim/flight_controls/pitch_trim_up",
    },
    # sim/flight_controls/pitch_trim_down
    {
        "control_type": PushButton,
        "touchosc_address": "/UNDEFINED",
        "xplane_command_address": "sim/flight_controls/pitch_trim_down",
    },
]
