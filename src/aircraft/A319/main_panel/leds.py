##########################################################################################
# MAIN PANEL LEDS
##########################################################################################

from lib.controls import Led

main_panel_leds = []

isi_baro_setting = [
    {"control_type": Led, "xplane_dref_address": "AirbusFBW/ALTmanaged", "touchosc_address": "/led/alt_managed",},
    {"control_type": Led, "xplane_dref_address": "AirbusFBW/HDGmanaged", "touchosc_address": "/led/hdg_managed",},
    {"control_type": Led, "xplane_dref_address": "AirbusFBW/SPDmanaged", "touchosc_address": "/led/spd_managed",},
]
main_panel_leds.extend(isi_baro_setting)
