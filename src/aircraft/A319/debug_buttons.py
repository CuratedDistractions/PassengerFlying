##########################################################################################
# DEBUG BUTTONS
##########################################################################################

from lib.controls import ToggleButton
import logging

# Create a logger object.
logger = logging.getLogger(__name__)

debug_buttons = []

dref = "AirbusFBW/N1ModeSwitchArray"
count = 4
button_start = 43

for i in range(64):
    if i > count - 1:
        break
    debug_buttons.extend(
        [
            {
                "control_type": ToggleButton,
                "touchosc_address": "/Debug/toggle" + str(button_start + i),
                "xplane_dref_address": dref,
                "xplane_dref_index": i,
            },
        ]
    )
