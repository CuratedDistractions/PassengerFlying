##########################################################################################
# DEBUG BUTTONS
##########################################################################################

from lib.controls import ToggleButton

debug_buttons = []

dref = "AirbusFBW/HydOHPArray"
count = 24
button_start = 43

for i in range(count):
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
