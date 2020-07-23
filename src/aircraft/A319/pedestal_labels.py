##########################################################################################
# PEDESTAL LABELS
##########################################################################################

from aircraft.A319.controls import AirbusLabel
import logging

# Create a logger object.
logger = logging.getLogger(__name__)

pedestal_labels = []


def set_xplane_dref_address_and_control_type(item_list: list, xplane_dref_address=None):
    for idx, item in enumerate(item_list):
        item_list[idx]["xplane_dref_address"] = xplane_dref_address
        item_list[idx]["control_type"] = AirbusLabel
    return item_list


# AirbusFBW/OHPLightsATA31[64] (also defined in overhead_panel_labels and main_panel_labels)
ohp_lights_ata31 = [
    {"xplane_dref_index": 30, "touchosc_address": "/label/eng",},
    {"xplane_dref_index": 31, "touchosc_address": "/label/bleed",},
    {"xplane_dref_index": 32, "touchosc_address": "/label/press",},
    {"xplane_dref_index": 33, "touchosc_address": "/label/elec",},
    {"xplane_dref_index": 34, "touchosc_address": "/label/hyd",},
    {"xplane_dref_index": 35, "touchosc_address": "/label/fuel",},
    {"xplane_dref_index": 36, "touchosc_address": "/label/apu",},
    {"xplane_dref_index": 37, "touchosc_address": "/label/cond",},
    {"xplane_dref_index": 38, "touchosc_address": "/label/door",},
    {"xplane_dref_index": 39, "touchosc_address": "/label/wheel",},
    {"xplane_dref_index": 40, "touchosc_address": "/label/f_ctl",},
    {"xplane_dref_index": 41, "touchosc_address": "/label/sts",},
    {"xplane_dref_index": 42, "touchosc_address": "/label/clr_left",},
    {"xplane_dref_index": 43, "touchosc_address": "/label/clr_right",},
]
logger.debug("Importing")

ohp_lights_ata31 = set_xplane_dref_address_and_control_type(ohp_lights_ata31, "AirbusFBW/OHPLightsATA31")
pedestal_labels.extend(ohp_lights_ata31)

# ! I Don't know why, but X-Plane crashes when using this dref
# AirbusFBW/ACP1Lights[16]
acp1_lights = [
    {"xplane_dref_index": 0, "touchosc_address": "/label/cpt_com_call_1"},
    {"xplane_dref_index": 1, "touchosc_address": "/label/cpt_com_call_2"},
]
logger.debug("Importing")
acp1_lights = set_xplane_dref_address_and_control_type(acp1_lights, "AirbusFBW/ACP1Lights")
# pedestal_labels.extend(acp1_lights)
