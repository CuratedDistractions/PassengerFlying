##########################################################################################
# MAIN PANEL BUTTONS
##########################################################################################

import logging

from lib.controls import PushButton

# Create a logger object.
logger = logging.getLogger(__name__)

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
logger.debug("Importing")
main_panel_buttons.extend(master_buttons)
