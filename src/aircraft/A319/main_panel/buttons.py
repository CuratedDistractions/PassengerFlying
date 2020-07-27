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
isi_baro_std = [
    {
        "control_type": AirbusQNHStandardButton,
        "touchosc_address": "/button/cpt_qnh",
        "xplane_dref_address": "AirbusFBW/BaroStdCapt",
    },
]
main_panel_buttons.extend(isi_baro_std)
