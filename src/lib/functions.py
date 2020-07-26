import argparse
import importlib
import coloredlogs
import logging
import socket
import sys
from packaging import version

# Create a logger object
logger = logging.getLogger(__name__)


def setup_logging(debug):
    # Setup logging
    verbose_level = "DEBUG" if debug else "WARNING"
    coloredlogs.install(
        fmt="%(asctime)s,%(msecs)d %(name)s(%(lineno)d) %(processName)s %(levelname)s %(funcName)s %(message)s",
        level=verbose_level,
    )


def parse_arguments(current_version):
    # Parse arguments
    parser = argparse.ArgumentParser(description=f"-== PassengerFlying v{current_version} ==-")

    parser.add_argument("--aircraft", required=True, help="Folder name of aircraft to load")
    parser.add_argument("--debug", help="Increase output verbosity", action="store_true")
    parser.add_argument("--touchosc_device_ip", required=True, help="IP address of TouchOSC device")
    parser.add_argument("--touchosc_device_port", help="Port of TouchOSC device", default=5006)
    parser.add_argument("--touchosc_server_ip", help="IP address of TouchOSC server", default="0.0.0.0")
    parser.add_argument("--touchosc_server_port", help="Port of TouchOSC server", default=5005)

    return parser.parse_args()


def load_aircraft_configuration(aircraft_name: str):
    # Check if we have a configuration for the loaded aircraft, if not we quit
    try:
        aircraft_module = ".".join(["aircraft", aircraft_name, "aircraft"])
        aircraft = importlib.import_module(aircraft_module).Aircraft()

    except ModuleNotFoundError as e:
        logger.error(f"Could not load aircraft configuration for {aircraft_name} ({e}).")
        sys.exit()

    return aircraft


def xplane_is_running(xplane) -> bool:
    """Check if X-Plane is running and an aircraft is loaded."""

    try:
        xplane.get_from_xplane("sim/aircraft/view/acf_ICAO")
    except socket.timeout as e:
        logger.error(f"Either X-Plane is't running or no aircraft was loaded ({e}).")
        sys.exit()

    return True


def aircraft_is_compatible(aircraft, current_version) -> bool:
    """Check compatability of aircraft configuration version with base script version."""

    try:
        if version.parse(current_version) < version.parse(aircraft.minimum_supported_version()) or version.parse(
            current_version
        ) > version.parse(aircraft.maximum_supported_version()):
            logger.error(
                "This aircraft is only compatible with PassengerFlying versions between {} and {}. You are using version {}".format(
                    aircraft.minimum_supported_version(), aircraft.maximum_supported_version(), current_version
                )
            )
            sys.exit()
    except AttributeError as e:
        logger.error(f"This aircraft has no version compatability configured ({e}).")
        sys.exit()

    return True


def decode_xplane_text(text):
    CHARACTERS = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "😳",
        "😳",
        "😳",
        "😳",
        "😳",
        "😳",
        "😳",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    result = ""

    try:
        for i in text:
            # We substract 48 from i because the first 48 characters in the list X-Plane uses are empty
            # And I don't want to add 48 bogus elements to my list above. :)
            corrected_index = int(i) - 48
            if corrected_index > 0:  # Can't request an index below 0
                result = "".join([result, CHARACTERS[corrected_index]])
        return result
    except IndexError as e:
        return f"EMPTY_STRING ({e})"
