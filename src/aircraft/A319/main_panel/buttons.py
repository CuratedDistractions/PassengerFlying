##########################################################################################
# MAIN PANEL BUTTONS
##########################################################################################

from lib.controls import PushButton

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

# AirbusFBW/ISIBaroStd