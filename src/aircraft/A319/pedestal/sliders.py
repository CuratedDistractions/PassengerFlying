##########################################################################################
# PEDESTAL SLIDERS
##########################################################################################

from aircraft.A319.controls import AirbusThrottle

pedestal_sliders = []

# sim/flightmodel/controls/flaprqst[1] (0, 0.25, 0.5, 0.75, 1)

# AirbusFBW/throttle_input[5]
throttle_input = [
    {
        "control_type": AirbusThrottle,
        "touchosc_address": "/fader/thrust_1",
        "xplane_dref_address": "AirbusFBW/throttle_input",
        "xplane_dref_index": 0,
    },
    {
        "control_type": AirbusThrottle,
        "touchosc_address": "/fader/thrust_2",
        "xplane_dref_address": "AirbusFBW/throttle_input",
        "xplane_dref_index": 1,
    },
    {
        "control_type": AirbusThrottle,
        "touchosc_address": "/fader/thrust_reverse_1",
        "xplane_dref_address": "AirbusFBW/throttle_input",
        "xplane_dref_index": 0,
    },
    {
        "control_type": AirbusThrottle,
        "touchosc_address": "/fader/thrust_reverse_2",
        "xplane_dref_address": "AirbusFBW/throttle_input",
        "xplane_dref_index": 1,
    },
]
pedestal_sliders.extend(throttle_input)
