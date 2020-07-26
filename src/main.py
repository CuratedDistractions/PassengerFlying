import logging
from multiprocessing import Process, freeze_support

from lib.functions import (
    parse_arguments,
    load_aircraft_configuration,
    xplane_is_running,
    aircraft_is_compatible,
    setup_logging,
)
from lib.settings import globals_list
from lib.touchosc import TouchOSC
from lib.xplane import XPlane

# Current version
CURRENT_VERSION = "0.1a"

logger = logging.getLogger(__name__)


def main():
    # Collect arguments from command line
    args = parse_arguments(CURRENT_VERSION)

    # Setup logging format
    setup_logging(args.debug)

    # Save the arguments list to the global variables list
    globals_list.args = args

    # Initialize force refresh setting
    globals_list.force_refresh = {}

    touchosc = TouchOSC()  # This class is responsible for the connection with TouchOSC
    globals_list.touchosc = touchosc  # Save the connection in a global list

    xplane = XPlane()  # This class is responsible for the connection with X-Plane
    globals_list.xplane = xplane  # Save the connection in a global list

    # Import modules of aircraft configuration
    aircraft = load_aircraft_configuration(args.aircraft)
    # Save the aircraft in a global list
    globals_list.aircraft = aircraft

    # Check if X-Plane is running and aircraft configuration is compatible with base script
    if xplane_is_running(xplane) and aircraft_is_compatible(aircraft, CURRENT_VERSION):
        logger.info(f"Loading of {args.aircraft} configuration successful.")

    # Let's start the show.
    run_loop(xplane, touchosc)


def run_loop(xplane, touchosc):
    # Start two parallel processes:
    # - one pulls drefs from X-Plane about 10 times per second
    xplane = Process(target=xplane.monitor, name="X-Plane")
    xplane.start()

    # - the other one listens for events from OSC
    touchosc = Process(target=touchosc.server, name="TouchOSC")
    touchosc.start()

    xplane.join()
    touchosc.join()


if __name__ == "__main__":
    freeze_support()  # Pyinstaller needs this to support multiprocessing
    main()
