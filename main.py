import argparse
import importlib
import logging
import socket
import sys
from multiprocessing import Process, freeze_support

import coloredlogs
from packaging import version

import lib.settings as settings
from lib.touchosc import TouchOSC
from lib.xplane import XPlane

# Current version
CURRENT_VERSION = "0.1a"

# Initialize things like the global variables list
settings.init()

# Parse arguments
parser = argparse.ArgumentParser(description=f"-== PassengerFlying v{CURRENT_VERSION} ==-")
parser.add_argument("--debug", help="increase output verbosity", action="store_true")
parser.add_argument("--touchosc_device_ip", help="IP address of TouchOSC device", default="192.168.2.9")
parser.add_argument("--touchosc_device_port", help="Port of TouchOSC device", default="5006")
parser.add_argument("--touchosc_server_port", help="Port of TouchOSC server", default="5005")
parser.add_argument("aircraft", help="folder name of aircraft to load")
args = parser.parse_args()
settings.globalList["ARGS"] = args

verbose_level = "DEBUG" if args.debug else "WARNING"

# Create a logger object.
logger = logging.getLogger(__name__)

# Set logging level and format
coloredlogs.install(
    fmt="%(asctime)s %(name)s %(levelname)s %(message)s", level=verbose_level,
)


def main():
    touchosc = TouchOSC()  # This class is responsible for the connection with TouchOSC
    settings.globalList["TOUCHOSC"] = touchosc  # Save the connection in a global list

    xplane = XPlane()  # This class is responsible for the connection with X-Plane
    settings.globalList["XPLANE"] = xplane  # Save the connection in a global list

    # Check if we have a configuration for the loaded aircraft, if not we quit
    try:
        aircraft_module = ".".join(["aircraft", args.aircraft, "aircraft"])
        aircraft = importlib.import_module(aircraft_module).Aircraft()

        # Save the aircraft in a global list
        settings.globalList["AIRCRAFT"] = aircraft
    except ModuleNotFoundError as e:
        logger.error(f"There is no configuration for ICAO {args.aircraft} ({e}).")
        sys.exit()

    # Check if X-Plane is running and an aircraft is loaded
    try:
        xplane.get_from_xplane("sim/aircraft/view/acf_ICAO")
    except socket.timeout as e:
        logger.error(f"Either X-Plane is't running or no aircraft was loaded ({e}).")
        sys.exit()

    try:
        if version.parse(CURRENT_VERSION) < version.parse(aircraft.minimum_supported_version()) or version.parse(
            CURRENT_VERSION
        ) > version.parse(aircraft.maximum_supported_version()):
            logger.error(
                "This aircraft is only compatible with PassengerFlying versions between {} and {}. You are using version {}".format(
                    aircraft.minimum_supported_version(), aircraft.maximum_supported_version(), CURRENT_VERSION
                )
            )
            sys.exit()
    except AttributeError as e:
        logger.error(f"This aircraft has no version compatability configured ({e}).")
        sys.exit()

    logger.info(f"Loading of {args.aircraft} configuration successful.")

    # TODO: Check if we can connect to TouchOSC, if not we quit

    # Start two parallel processes:
    # - one pulls drefs from X-Plane about 10 times per second
    monitor = Process(target=xplane.monitor)
    monitor.start()

    # - the other one listens for events from OSC
    server = Process(target=touchosc.server)
    server.start()

    monitor.join()
    server.join()


if __name__ == "__main__":
    freeze_support()  # Pyinstaller needs this to support multiprocessing
    main()
