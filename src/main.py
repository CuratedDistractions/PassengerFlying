import logging
from multiprocessing import Process, freeze_support

from lib.functions import (
    aircraft_is_compatible,
    load_aircraft_configuration,
    parse_arguments,
    setup_logging,
    xplane_is_running,
)
from lib.settings import globals_list
from lib.touchosc import TouchOSC
from lib.xplane import XPlane

# Current version
CURRENT_VERSION = "0.1a"

logger = logging.getLogger(__name__)


def main():
    # Collect arguments from command line
    parse_arguments(CURRENT_VERSION)

    # Setup logging format
    setup_logging()

    # Initialize some variables
    globals_list.force_refresh = {}

    touchosc = TouchOSC()  # This class is responsible for the connection with TouchOSC
    globals_list.touchosc = touchosc  # Save the connection in a global list

    xplane = XPlane()  # This class is responsible for the connection with X-Plane
    globals_list.xplane = xplane  # Save the connection in a global list
    globals_list.current_version = CURRENT_VERSION

    # Import modules of aircraft configuration
    load_aircraft_configuration()

    # Check if X-Plane is running and aircraft configuration is compatible with base script
    if xplane_is_running() and aircraft_is_compatible():
        logger.info(f"Loading of {globals_list.args.aircraft} configuration successful.")

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
