##########################################################################################
"""     OVERHEAD PANEL LABELS """
##########################################################################################

from aircraft.A319.controls import AirbusButtonLabel
from lib.controls import DynamicLabel

# Some constants for TouchOSC
RED = "red"
GREEN = "green"
BLUE = "blue"
YELLOW = "yellow"
PURPLE = "purple"
GRAY = "gray"
GREY = "gray"
ORANGE = "orange"
BROWN = "brown"
PINK = "pink"

overhead_panel_labels = []


def set_xplane_dref_address_and_control_type(item_list: list, xplane_dref_address=None):
    for idx, item in enumerate(item_list):
        item_list[idx]["xplane_dref_address"] = xplane_dref_address
        item_list[idx]["control_type"] = AirbusButtonLabel
    return item_list


# AirbusFBW/OHPLightsATA21
ohp_lights_ata21 = [
    {
        "xplane_dref_index": 0,
        "touchosc_address": "/ovhd/label406",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "ENG 1 BLEED",
    },
    {
        "xplane_dref_index": 1,
        "touchosc_address": "/ovhd/label407",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "ENG 1 BLEED",
    },
    {
        "xplane_dref_index": 2,
        "touchosc_address": "/ovhd/label467",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "ENG 2 BLEED",
    },
    {
        "xplane_dref_index": 3,
        "touchosc_address": "/ovhd/label468",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "ENG 2 BLEED",
    },
    {
        "xplane_dref_index": 4,
        "touchosc_address": "/ovhd/label412",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": BLUE,
        "remarks": "APU BLEED",
    },
    {
        "xplane_dref_index": 5,
        "touchosc_address": "/ovhd/label413",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "APU BLEED",
    },
    {
        "xplane_dref_index": 6,
        "touchosc_address": "/ovhd/label403",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "PACK 1",
    },
    {
        "xplane_dref_index": 7,
        "touchosc_address": "/ovhd/label404",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "PACK 1",
    },
    {
        "xplane_dref_index": 8,
        "touchosc_address": "/ovhd/label458",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "PACK 2",
    },
    {
        "xplane_dref_index": 9,
        "touchosc_address": "/ovhd/label459",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "PACK 2",
    },
    {
        "xplane_dref_index": 10,
        "touchosc_address": "/ovhd/label397",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "AIR COND - HOT AIR",
    },
    {
        "xplane_dref_index": 11,
        "touchosc_address": "/ovhd/label398",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "AIR COND - HOT AIR",
    },
    {
        "xplane_dref_index": 12,
        "touchosc_address": "/ovhd/label409",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": GREY,
        "remarks": "RAM AIR",
    },
    # {
    #     "xplane_dref_index": 13,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "ON",
    #     "touchosc_initial_color": GREY,
    #     "remarks": "DITCHING",
    # },
    # {
    #     "xplane_dref_index": 14,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "MAN",
    #     "touchosc_initial_color": GREY,
    #     "remarks": "CABIN PRESS - MODE SEL",
    # },
    # {"xplane_dref_index": 15, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    {
        "xplane_dref_index": 16,
        "touchosc_address": "/ovhd/label274",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "CAB FANS",
    },
    {
        "xplane_dref_index": 17,
        "touchosc_address": "/ovhd/label272",
        "touchosc_initial_text": "OVRD",
        "touchosc_initial_color": GREY,
        "remarks": "EXTRACT",
    },
    {
        "xplane_dref_index": 18,
        "touchosc_address": "/ovhd/label273",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "EXTRACT",
    },
    {
        "xplane_dref_index": 19,
        "touchosc_address": "/ovhd/label270",
        "touchosc_initial_text": "OVRD",
        "touchosc_initial_color": GREY,
        "remarks": "BLOWER",
    },
    {
        "xplane_dref_index": 20,
        "touchosc_address": "/ovhd/label271",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "BLOWER",
    },
    {
        "xplane_dref_index": 21,
        "touchosc_address": "/ovhd/label256",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "FWD ISOL VALVE",
    },
    {
        "xplane_dref_index": 22,
        "touchosc_address": "/ovhd/label257",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "FWD ISOL VALVE",
    },
    {
        "xplane_dref_index": 23,
        "touchosc_address": "/ovhd/label260",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "AFT ISOL VALVE",
    },
    {
        "xplane_dref_index": 24,
        "touchosc_address": "/ovhd/label261",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "AFT ISOL VALVE",
    },
    {
        "xplane_dref_index": 25,
        "touchosc_address": "/ovhd/label258",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "HOT AIR",
    },
    {
        "xplane_dref_index": 26,
        "touchosc_address": "/ovhd/label259",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "HOT AIR",
    },
    # {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
]
# Add xplane_dref to this list
ohp_lights_ata21 = set_xplane_dref_address_and_control_type(ohp_lights_ata21, "AirbusFBW/OHPLightsATA21")
overhead_panel_labels.extend(ohp_lights_ata21)

# AirbusFBW/OHPLightsATA24
ohp_lights_ata24 = [
    {
        "xplane_dref_index": 0,
        "touchosc_address": "/ovhd/label330",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "GEN 1",
    },
    {
        "xplane_dref_index": 1,
        "touchosc_address": "/ovhd/label331",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "GEN 1",
    },
    {
        "xplane_dref_index": 2,
        "touchosc_address": "/ovhd/label344",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "GEN 2",
    },
    {
        "xplane_dref_index": 3,
        "touchosc_address": "/ovhd/label345",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "GEN 2",
    },
    {
        "xplane_dref_index": 4,
        "touchosc_address": "/ovhd/label332",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "APU GEN",
    },
    {
        "xplane_dref_index": 5,
        "touchosc_address": "/ovhd/label333",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "APU GEN",
    },
    {
        "xplane_dref_index": 6,
        "touchosc_address": "/ovhd/label336",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": BLUE,
        "remarks": "EXT PWR",
    },
    {
        "xplane_dref_index": 7,
        "touchosc_address": "/ovhd/label337",
        "touchosc_initial_text": "AVAIL",
        "touchosc_initial_color": GREEN,
        "remarks": "EXT PWR",
    },
    {
        "xplane_dref_index": 8,
        "touchosc_address": "/ovhd/label334",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "BUS TIE",
    },
    {
        "xplane_dref_index": 9,
        "touchosc_address": "/ovhd/label338",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "BAT 1",
    },
    {
        "xplane_dref_index": 10,
        "touchosc_address": "/ovhd/label339",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "BAT 1",
    },
    {
        "xplane_dref_index": 11,
        "touchosc_address": "/ovhd/label340",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "BAT 2",
    },
    {
        "xplane_dref_index": 12,
        "touchosc_address": "/ovhd/label341",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "BAT 2",
    },
    {
        "xplane_dref_index": 13,
        "touchosc_address": "/ovhd/label342",
        "touchosc_initial_text": "ALTN",
        "touchosc_initial_color": GREY,
        "remarks": "AC ESS FEED",
    },
    {
        "xplane_dref_index": 14,
        "touchosc_address": "/ovhd/label343",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "AC ESS FEED",
    },
    {
        "xplane_dref_index": 15,
        "touchosc_address": "/ovhd/label324",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "Commercial",
    },
    {
        "xplane_dref_index": 16,
        "touchosc_address": "/ovhd/label326",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "Galley",
    },
    {
        "xplane_dref_index": 17,
        "touchosc_address": "/ovhd/label327",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "Galley",
    },
    # {"xplane_dref_index": 18, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 19, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 20, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {
    #     "xplane_dref_index": 21,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "OFF",
    #     "touchosc_initial_color": GREY,
    #     "remarks": "GEN 1 LINE",
    # },
    # {"xplane_dref_index": 22, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
]
# Add xplane_dref to this list
ohp_lights_ata24 = set_xplane_dref_address_and_control_type(ohp_lights_ata24, "AirbusFBW/OHPLightsATA24")
overhead_panel_labels.extend(ohp_lights_ata24)

# # AirbusFBW/OHPLightsATA26
# ohp_lights_ata26 = [
#     {"xplane_dref_index": 0, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "FIRE", "remarks": "ENG 1 - FIRE",},
#     {
#         "xplane_dref_index": 1,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "DISCH",
#         "touchosc_initial_color": ORANGE,
#         "remarks": "ENG 1 - AGENT 1",
#     },
#     {
#         "xplane_dref_index": 2,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "SOLIB",
#         "touchosc_initial_color": GREY,
#         "remarks": "ENG 1 - AGENT 1",
#     },
#     {
#         "xplane_dref_index": 3,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "DISCH",
#         "touchosc_initial_color": ORANGE,
#         "remarks": "ENG 1 - AGENT 2",
#     },
#     {
#         "xplane_dref_index": 4,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "SOLIB",
#         "touchosc_initial_color": GREY,
#         "remarks": "ENG 1 - AGENT 2",
#     },
#     {"xplane_dref_index": 5, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "FIRE", "remarks": "ENG 2 - FIRE",},
#     {
#         "xplane_dref_index": 6,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "DISCH",
#         "touchosc_initial_color": ORANGE,
#         "remarks": "ENG 2 - AGENT 1",
#     },
#     {
#         "xplane_dref_index": 7,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "SOLIB",
#         "touchosc_initial_color": GREY,
#         "remarks": "ENG 2 - AGENT 1",
#     },
#     {
#         "xplane_dref_index": 8,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "DISCH",
#         "remarks": "ENG 2 - AGENT 2",
#     },
#     {
#         "xplane_dref_index": 9,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "SOLIB",
#         "touchosc_initial_color": GREY,
#         "remarks": "ENG 2 - AGENT 2",
#     },
#     {"xplane_dref_index": 20, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {"xplane_dref_index": 21, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {
#         "xplane_dref_index": 22,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "SOLIB",
#         "touchosc_initial_color": GREY,
#         "remarks": "APU - AGENT",
#     },
#     {"xplane_dref_index": 23, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {"xplane_dref_index": 24, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {"xplane_dref_index": 25, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {"xplane_dref_index": 26, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
# ]
# # Add xplane_dref to this list
# ohp_lights_ata26 = set_xplane_dref_address_and_control_type(ohp_lights_ata26, "AirbusFBW/OHPLightsATA26")
# overhead_panel_labels.extend(ohp_lights_ata26)

# AirbusFBW/OHPLightsATA27
ohp_lights_ata27 = [
    {
        "xplane_dref_index": 0,
        "touchosc_address": "/ovhd/label193",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "ELAC 1",
    },
    {
        "xplane_dref_index": 1,
        "touchosc_address": "/ovhd/label194",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "ELAC 1",
    },
    {
        "xplane_dref_index": 2,
        "touchosc_address": "/ovhd/label249",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "ELAC 2",
    },
    {
        "xplane_dref_index": 3,
        "touchosc_address": "/ovhd/label250",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "ELAC 2",
    },
    {
        "xplane_dref_index": 4,
        "touchosc_address": "/ovhd/label195",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "SEC 1",
    },
    {
        "xplane_dref_index": 5,
        "touchosc_address": "/ovhd/label196",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "SEC 1",
    },
    {
        "xplane_dref_index": 6,
        "touchosc_address": "/ovhd/label247",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "SEC 2",
    },
    {
        "xplane_dref_index": 7,
        "touchosc_address": "/ovhd/label248",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "SEC 2",
    },
    {
        "xplane_dref_index": 8,
        "touchosc_address": "/ovhd/label245",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "SEC 3",
    },
    {
        "xplane_dref_index": 9,
        "touchosc_address": "/ovhd/label246",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "SEC 3",
    },
    {
        "xplane_dref_index": 10,
        "touchosc_address": "/ovhd/label197",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "FAC 1",
    },
    {
        "xplane_dref_index": 11,
        "touchosc_address": "/ovhd/label198",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "FAC 1",
    },
    {
        "xplane_dref_index": 12,
        "touchosc_address": "/ovhd/label243",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "FAC 2",
    },
    {
        "xplane_dref_index": 13,
        "touchosc_address": "/ovhd/label244",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "FAC 2",
    },
    # {"xplane_dref_index": 20, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 21, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 22, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 23, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
]
# Add xplane_dref to this list
ohp_lights_ata27 = set_xplane_dref_address_and_control_type(ohp_lights_ata27, "AirbusFBW/OHPLightsATA27")
overhead_panel_labels.extend(ohp_lights_ata27)

# AirbusFBW/OHPLightsATA28
ohp_lights_ata28 = [
    {
        "xplane_dref_index": 0,
        "touchosc_address": "/ovhd/label308",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "LTK PUMPS 1",
    },
    {
        "xplane_dref_index": 1,
        "touchosc_address": "/ovhd/label309",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "LTK PUMPS 1",
    },
    {
        "xplane_dref_index": 2,
        "touchosc_address": "/ovhd/label310",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "LTK PUMPS 2",
    },
    {
        "xplane_dref_index": 3,
        "touchosc_address": "/ovhd/label311",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "LTK PUMPS 2",
    },
    {
        "xplane_dref_index": 4,
        "touchosc_address": "/ovhd/label312",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "Pump 1",
    },
    {
        "xplane_dref_index": 5,
        "touchosc_address": "/ovhd/label313",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "Pump 1",
    },
    {
        "xplane_dref_index": 6,
        "touchosc_address": "/ovhd/label316",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "Pump 2",
    },
    {
        "xplane_dref_index": 7,
        "touchosc_address": "/ovhd/label317",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "Pump 2",
    },
    {
        "xplane_dref_index": 8,
        "touchosc_address": "/ovhd/label318",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "RTK PUMPS 1",
    },
    {
        "xplane_dref_index": 9,
        "touchosc_address": "/ovhd/label319",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "RTK PUMPS 1",
    },
    {
        "xplane_dref_index": 10,
        "touchosc_address": "/ovhd/label320",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "RTK PUMPS 2",
    },
    {
        "xplane_dref_index": 11,
        "touchosc_address": "/ovhd/label321",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "RTK PUMPS 2",
    },
    {
        "xplane_dref_index": 12,
        "touchosc_address": "/ovhd/label314",
        "touchosc_initial_text": "MAN",
        "touchosc_initial_color": GREY,
        "remarks": "MODE SEL",
    },
    {
        "xplane_dref_index": 13,
        "touchosc_address": "/ovhd/label315",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "MODE SEL",
    },
    {
        "xplane_dref_index": 14,
        "touchosc_address": "/ovhd/label322",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": GREY,
        "remarks": "X FEED",
    },
    {
        "xplane_dref_index": 15,
        "touchosc_address": "/ovhd/label323",
        "touchosc_initial_text": "OPEN",
        "touchosc_initial_color": GREEN,
        "remarks": "X FEED",
    },
    # {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
]
# Add xplane_dref to this list
ohp_lights_ata28 = set_xplane_dref_address_and_control_type(ohp_lights_ata28, "AirbusFBW/OHPLightsATA28")
overhead_panel_labels.extend(ohp_lights_ata28)

# AirbusFBW/OHPLightsATA29
ohp_lights_ata29 = [
    {
        "xplane_dref_index": 0,
        "touchosc_address": "/ovhd/label298",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "ENG 1 PUMP",
    },
    {
        "xplane_dref_index": 1,
        "touchosc_address": "/ovhd/label299",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "ENG 1 PUMP",
    },
    {
        "xplane_dref_index": 2,
        "touchosc_address": "/ovhd/label304",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "ENG 2 PUMP",
    },
    {
        "xplane_dref_index": 3,
        "touchosc_address": "/ovhd/label305",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "ENG 2 PUMP",
    },
    {
        "xplane_dref_index": 4,
        "touchosc_address": "/ovhd/label300",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "BLUE - ELEC PUMP",
    },
    {
        "xplane_dref_index": 5,
        "touchosc_address": "/ovhd/label301",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "BLUE - ELEC PUMP",
    },
    {
        "xplane_dref_index": 6,
        "touchosc_address": "/ovhd/label306",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": GREY,
        "remarks": "YELLOW - ELEC PUMP",
    },
    {
        "xplane_dref_index": 7,
        "touchosc_address": "/ovhd/label307",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "YELLOW - ELEC PUMP",
    },
    {
        "xplane_dref_index": 8,
        "touchosc_address": "/ovhd/label302",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "PTU",
    },
    {
        "xplane_dref_index": 9,
        "touchosc_address": "/ovhd/label303",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "PTU",
    },
    # {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
]
# Add xplane_dref to this list
ohp_lights_ata29 = set_xplane_dref_address_and_control_type(ohp_lights_ata29, "AirbusFBW/OHPLightsATA29")
overhead_panel_labels.extend(ohp_lights_ata29)

# AirbusFBW/OHPLightsATA30
ohp_lights_ata30 = [
    {
        "xplane_dref_index": 0,
        "touchosc_address": "/ovhd/label441",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": BLUE,
        "remarks": "WING",
    },
    {
        "xplane_dref_index": 1,
        "touchosc_address": "/ovhd/label442",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "WING",
    },
    {
        "xplane_dref_index": 2,
        "touchosc_address": "/ovhd/label444",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": BLUE,
        "remarks": "ENG 1",
    },
    {
        "xplane_dref_index": 3,
        "touchosc_address": "/ovhd/label445",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "ENG 1",
    },
    {
        "xplane_dref_index": 4,
        "touchosc_address": "/ovhd/label447",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": BLUE,
        "remarks": "ENG 2",
    },
    {
        "xplane_dref_index": 5,
        "touchosc_address": "/ovhd/label448",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "ENG 2",
    },
    {
        "xplane_dref_index": 10,
        "touchosc_address": "/ovhd/label450",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": BLUE,
        "remarks": "PROBE/WINDOW HEAT",
    },
    # {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
]
# Add xplane_dref to this list
ohp_lights_ata30 = set_xplane_dref_address_and_control_type(ohp_lights_ata30, "AirbusFBW/OHPLightsATA30")
overhead_panel_labels.extend(ohp_lights_ata30)

# AirbusFBW/OHPLightsATA31
ohp_lights_ata31 = [
    # {
    #     "xplane_dref_index": 0,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "MASTER",
    #     "touchosc_initial_color": RED,
    #     "remarks": "CPT - MASTER WARN",
    # },
    # {
    #     "xplane_dref_index": 1,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "WARN",
    #     "touchosc_initial_color": RED,
    #     "remarks": "CPT - MASTER WARN",
    # },
    # {
    #     "xplane_dref_index": 2,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "MASTER",
    #     "touchosc_initial_color": RED,
    #     "remarks": "FO - MASTER WARN",
    # },
    # {
    #     "xplane_dref_index": 3,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "WARN",
    #     "touchosc_initial_color": RED,
    #     "remarks": "FO - MASTER WARN",
    # },
    # {
    #     "xplane_dref_index": 4,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "MASTER",
    #     "touchosc_initial_color": YELLOW,
    #     "remarks": "CPT - MASTER CAUT",
    # },
    # {
    #     "xplane_dref_index": 5,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "CAUT",
    #     "touchosc_initial_color": YELLOW,
    #     "remarks": "CPT - MASTER CAUT",
    # },
    # {
    #     "xplane_dref_index": 6,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "MASTER",
    #     "touchosc_initial_color": YELLOW,
    #     "remarks": "FO - MASTER CAUT",
    # },
    # {
    #     "xplane_dref_index": 7,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "CAUT",
    #     "touchosc_initial_color": YELLOW,
    #     "remarks": "FO - MASTER CAUT",
    # },
    # {"xplane_dref_index": 8, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 9, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 10, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "EVAC/ON", "remarks": "COMMAND",},
    # {"xplane_dref_index": 11, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "EVAC/ON", "remarks": "COMMAND",},
    {
        "xplane_dref_index": 12,
        "touchosc_address": "/ovhd/label427",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": ORANGE,
        "remarks": "EMER EXIT LT",
    },
    {
        "xplane_dref_index": 13,
        "touchosc_address": "/ovhd/label543",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": GREY,
        "remarks": "EMER",
    },
    {
        "xplane_dref_index": 14,
        "touchosc_address": "/ovhd/label544",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "EMER",
    },
    # {
    #     "xplane_dref_index": 15,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "ON",
    #     "touchosc_initial_color": BLUE,
    #     "remarks": "GND CTL",
    # },
    # {
    #     "xplane_dref_index": 16,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - CSTR",
    # },
    # {
    #     "xplane_dref_index": 17,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - WPT",
    # },
    # {
    #     "xplane_dref_index": 18,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - VOR,D",
    # },
    # {
    #     "xplane_dref_index": 19,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - NDB",
    # },
    # {
    #     "xplane_dref_index": 20,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - ARPT",
    # },
    # {
    #     "xplane_dref_index": 21,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - ARPT",
    # },
    # {
    #     "xplane_dref_index": 22,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - NDB",
    # },
    # {
    #     "xplane_dref_index": 23,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - VOR,D",
    # },
    # {
    #     "xplane_dref_index": 24,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - WPT",
    # },
    # {
    #     "xplane_dref_index": 25,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - CSTR",
    # },
    # {
    #     "xplane_dref_index": 26,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - FD",
    # },
    # {
    #     "xplane_dref_index": 27,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - FD",
    # },
    # {
    #     "xplane_dref_index": 28,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - LS",
    # },
    # {
    #     "xplane_dref_index": 29,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - LS",
    # },
    # {
    #     "xplane_dref_index": 30,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "ENG",
    # },
    # {
    #     "xplane_dref_index": 31,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "BLEED",
    # },
    # {
    #     "xplane_dref_index": 32,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "PRESS",
    # },
    # {
    #     "xplane_dref_index": 33,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "ELEC",
    # },
    # {
    #     "xplane_dref_index": 34,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "HYD",
    # },
    # {
    #     "xplane_dref_index": 35,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FUEL",
    # },
    # {
    #     "xplane_dref_index": 36,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "APU",
    # },
    # {
    #     "xplane_dref_index": 37,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "COND",
    # },
    # {
    #     "xplane_dref_index": 38,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "DOOR",
    # },
    # {
    #     "xplane_dref_index": 39,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "WHEEL",
    # },
    # {
    #     "xplane_dref_index": 40,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "F/CTL",
    # },
    # {
    #     "xplane_dref_index": 41,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "STS",
    # },
    # {
    #     "xplane_dref_index": 42,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CLR (left)",
    # },
    # {
    #     "xplane_dref_index": 43,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CLR (right)",
    # },
    # {
    #     "xplane_dref_index": 44,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "AP 1",
    # },
    # {
    #     "xplane_dref_index": 45,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "AP 2",
    # },
    # {"xplane_dref_index": 46, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 47, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {
    #     "xplane_dref_index": 48,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "====",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "APPR",
    # },
    # {"xplane_dref_index": 49, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 50, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
]
# Add xplane_dref to this list
ohp_lights_ata31 = set_xplane_dref_address_and_control_type(ohp_lights_ata31, "AirbusFBW/OHPLightsATA31")
overhead_panel_labels.extend(ohp_lights_ata31)

# # AirbusFBW/OHPLightsATA32
# ohp_lights_ata32 = [
#     {
#         "xplane_dref_index": 0,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "V",
#         "touchosc_initial_color": GREEN,
#         "remarks": "LDG GEAR 1",
#     },
#     {
#         "xplane_dref_index": 1,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "UNLK",
#         "touchosc_initial_color": RED,
#         "remarks": "LDG GEAR 1",
#     },
#     {
#         "xplane_dref_index": 2,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "V",
#         "touchosc_initial_color": GREEN,
#         "remarks": "LDG GEAR 2",
#     },
#     {
#         "xplane_dref_index": 3,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "UNLK",
#         "touchosc_initial_color": RED,
#         "remarks": "LDG GEAR 2",
#     },
#     {
#         "xplane_dref_index": 4,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "V",
#         "touchosc_initial_color": GREEN,
#         "remarks": "LDG GEAR 3",
#     },
#     {
#         "xplane_dref_index": 5,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "UNLK",
#         "touchosc_initial_color": RED,
#         "remarks": "LDG GEAR 3",
#     },
#     {
#         "xplane_dref_index": 10,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "ON",
#         "touchosc_initial_color": GREY,
#         "remarks": "BRK FAN",
#     },
#     {"xplane_dref_index": 11, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {
#         "xplane_dref_index": 12,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "ON",
#         "touchosc_initial_color": BLUE,
#         "remarks": "AUTO/BRK - LO",
#     },
#     {"xplane_dref_index": 13, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {
#         "xplane_dref_index": 14,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "ON",
#         "touchosc_initial_color": BLUE,
#         "remarks": "AUTO/BRK - MED",
#     },
#     {"xplane_dref_index": 15, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {
#         "xplane_dref_index": 16,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "ON",
#         "touchosc_initial_color": BLUE,
#         "remarks": "AUTO/BRK - MAX",
#     },
#     {"xplane_dref_index": 17, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
# ]
# # Add xplane_dref to this list
# ohp_lights_ata32 = set_xplane_dref_address_and_control_type(ohp_lights_ata32, "AirbusFBW/OHPLightsATA32")
# overhead_panel_labels.extend(ohp_lights_ata32)

# AirbusFBW/OHPLightsATA34
ohp_lights_ata34 = [
    {
        "xplane_dref_index": 0,
        "touchosc_address": "/ovhd/label237",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "ADR1",
    },
    {
        "xplane_dref_index": 1,
        "touchosc_address": "/ovhd/label238",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "ADR1",
    },
    {
        "xplane_dref_index": 2,
        "touchosc_address": "/ovhd/label239",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "ADR2",
    },
    {
        "xplane_dref_index": 3,
        "touchosc_address": "/ovhd/label240",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "ADR2",
    },
    {
        "xplane_dref_index": 4,
        "touchosc_address": "/ovhd/label241",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "ADR3",
    },
    {
        "xplane_dref_index": 5,
        "touchosc_address": "/ovhd/label242",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "ADR3",
    },
    {
        "xplane_dref_index": 6,
        "touchosc_address": "/ovhd/label231",
        "touchosc_initial_text": "ALIGN",
        "touchosc_initial_color": GREY,
        "remarks": "IR1",
    },
    {
        "xplane_dref_index": 7,
        "touchosc_address": "/ovhd/label232",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "IR1",
    },
    {
        "xplane_dref_index": 8,
        "touchosc_address": "/ovhd/label235",
        "touchosc_initial_text": "ALIGN",
        "touchosc_initial_color": GREY,
        "remarks": "IR2",
    },
    {
        "xplane_dref_index": 9,
        "touchosc_address": "/ovhd/label236",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "IR2",
    },
    {
        "xplane_dref_index": 10,
        "touchosc_address": "/ovhd/label233",
        "touchosc_initial_text": "ALIGN",
        "touchosc_initial_color": GREY,
        "remarks": "IR3",
    },
    {
        "xplane_dref_index": 11,
        "touchosc_address": "/ovhd/label234",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "IR3",
    },
    {
        "xplane_dref_index": 12,
        "touchosc_address": "/ovhd/label91",
        "touchosc_initial_text": "ON BAT",
        "touchosc_initial_color": ORANGE,
        "remarks": "ADIRS - BATTERY",
    },
    {
        "xplane_dref_index": 13,
        "touchosc_address": "/ovhd/label211",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "GPWS - SYS",
    },
    {
        "xplane_dref_index": 14,
        "touchosc_address": "/ovhd/label212",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "GPWS - SYS",
    },
    {
        "xplane_dref_index": 15,
        "touchosc_address": "/ovhd/label213",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "G/S MODE",
    },
    {
        "xplane_dref_index": 16,
        "touchosc_address": "/ovhd/label215",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "FLAP MODE",
    },
    {
        "xplane_dref_index": 17,
        "touchosc_address": "/ovhd/label217",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": GREY,
        "remarks": "LDG FLAP 3",
    },
    # {"xplane_dref_index": 20, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 21, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 22, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {"xplane_dref_index": 23, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
    # {
    #     "xplane_dref_index": 24,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "ON",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "CPT - TERR ON ND",
    # },
    # {
    #     "xplane_dref_index": 25,
    #     "touchosc_address": "/ovhd/label",
    #     "touchosc_initial_text": "ON",
    #     "touchosc_initial_color": GREEN,
    #     "remarks": "FO - TERR ON ND",
    # },
    {
        "xplane_dref_index": 26,
        "touchosc_address": "/ovhd/label209",
        "touchosc_initial_text": "OFF",
        "touchosc_initial_color": GREY,
        "remarks": "GPWS - TERR",
    },
    {
        "xplane_dref_index": 27,
        "touchosc_address": "/ovhd/label210",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "GPWS - TERR",
    },
    # {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
]
# Add xplane_dref to this list
ohp_lights_ata34 = set_xplane_dref_address_and_control_type(ohp_lights_ata34, "AirbusFBW/OHPLightsATA34")
overhead_panel_labels.extend(ohp_lights_ata34)

# # AirbusFBW/OHPLightsATA35
# ohp_lights_ata35 = [
#     {"xplane_dref_index": 0, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {
#         "xplane_dref_index": 1,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "OFF",
#         "touchosc_initial_color": GREY,
#         "remarks": "CREW SUPPLY",
#     },
#     {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
# ]
# # Add xplane_dref to this list
# ohp_lights_ata35 = set_xplane_dref_address_and_control_type(ohp_lights_ata35, "AirbusFBW/OHPLightsATA35")
# overhead_panel_labels.extend(ohp_lights_ata35)

# AirbusFBW/OHPLightsATA49
ohp_lights_ata49 = [
    {
        "xplane_dref_index": 0,
        "touchosc_address": "/ovhd/label420",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": BLUE,
        "remarks": "APU - MASTER SW",
    },
    {
        "xplane_dref_index": 1,
        "touchosc_address": "/ovhd/label421",
        "touchosc_initial_text": "FAULT",
        "touchosc_initial_color": ORANGE,
        "remarks": "APU - MASTER SW",
    },
    {
        "xplane_dref_index": 2,
        "touchosc_address": "/ovhd/label423",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": BLUE,
        "remarks": "APU - START",
    },
    {
        "xplane_dref_index": 3,
        "touchosc_address": "/ovhd/label424",
        "touchosc_initial_text": "AVAIL",
        "touchosc_initial_color": GREEN,
        "remarks": "APU - START",
    },
    # {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
]
# Add xplane_dref to this list
ohp_lights_ata49 = set_xplane_dref_address_and_control_type(ohp_lights_ata49, "AirbusFBW/OHPLightsATA49")
overhead_panel_labels.extend(ohp_lights_ata49)

# sim/cockpit2/electrical/battery_voltage_indicated_volts
battery_voltage_indicated_volts = [
    {
        "control_type": DynamicLabel,
        "xplane_dref_address": "AirbusFBW/BatVolts",
        "xplane_dref_index": 0,
        "touchosc_address": "/battery_voltage_1",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": GREY,
        "remarks": "BATT VOLT 1",
    },
    {
        "control_type": DynamicLabel,
        "xplane_dref_address": "AirbusFBW/BatVolts",
        "xplane_dref_index": 1,
        "touchosc_address": "/battery_voltage_2",
        "touchosc_initial_text": "ON",
        "touchosc_initial_color": GREY,
        "remarks": "BATT VOLT 1",
    },
]
# Add xplane_dref to this list
overhead_panel_labels.extend(battery_voltage_indicated_volts)


# # AirbusFBW/OHPLightsATA70
# ohp_lights_ata70 = [
#     {
#         "xplane_dref_index": 0,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "ON",
#         "touchosc_initial_color": BLUE,
#         "remarks": "MAN START - 1",
#     },
#     {
#         "xplane_dref_index": 1,
#         "touchosc_address": "/ovhd/label",
#         "touchosc_initial_text": "ON",
#         "touchosc_initial_color": BLUE,
#         "remarks": "MAN START - 2",
#     },
#     {"xplane_dref_index": 4, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {"xplane_dref_index": 5, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {"xplane_dref_index": 10, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {"xplane_dref_index": 11, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {"xplane_dref_index": 12, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {"xplane_dref_index": 13, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
#     {"xplane_dref_index": 63, "touchosc_address": "/ovhd/label", "touchosc_initial_text": "NONE",},
# ]
# # Add xplane_dref to this list
# ohp_lights_ata70 = set_xplane_dref_address_and_control_type(ohp_lights_ata70, "AirbusFBW/OHPLightsATA70")
# overhead_panel_labels.extend(ohp_lights_ata70)

# acp1_lights = LabelsArray(
#     xplane_dref="AirbusFBW/ACP1Lights",
#     name:"acp1_lights",
#     touchosc_labels_dict=[
#         {"xplane_dref_index": 0,   address:"/ovhd/label",   text:"====",    color:GREEN,   visible:True,    name:"CALL",},
#         {"xplane_dref_index": 1,   address:"/ovhd/label",   text:"====",    color:GREEN,   visible:True,    name:"CALL",},
#         {"xplane_dref_index": 2,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 3,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 4,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 5,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 6,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 7,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 8,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 9,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 17,   address:"/ovhd/label",    text:"NONE",     color:PINK,    visible:True,    name:"Unknown",},
#     ],
# )
# self.add_control(acp1_lights)

# acp2_lights = LabelsArray(
#     xplane_dref="AirbusFBW/ACP2Lights",
#     name:"acp2_lights",
#     touchosc_labels_dict=[
#         {"xplane_dref_index": 0,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 1,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 2,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 3,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 4,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 5,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 6,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 7,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 8,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 9,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 17,   address:"/ovhd/label",    text:"NONE",     color:PINK,    visible:True,    name:"Unknown",},
#     ],
# )
# self.add_control(acp2_lights)

# acp3_lights = LabelsArray(
#     xplane_dref="AirbusFBW/ACP3Lights",
#     name:"acp3_lights",
#     touchosc_labels_dict=[
#         {"xplane_dref_index": 0,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 1,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 2,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 3,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 4,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 5,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 6,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 7,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 8,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 9,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 17,   address:"/ovhd/label",    text:"NONE",     color:PINK,    visible:True,    name:"Unknown",},
#     ],
# )
# self.add_control(acp3_lights)

# adr_lights = LabelsArray(
#     xplane_dref="AirbusFBW/ADRLights",
#     name:"adr_lights",
#     touchosc_labels_dict=[
#         {"xplane_dref_index": 0,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 1,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 2,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 3,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 4,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#         {"xplane_dref_index": 5,   address:"/ovhd/label",   text:"NONE",    color:PINK,   visible:True,    name:"Unknown",},
#     ],
# )
# self.add_control(adr_lights)
