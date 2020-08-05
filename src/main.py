import asyncio
import logging
import time
from multiprocessing import freeze_support

from lib.functions import (
    aircraft_is_compatible,
    load_aircraft_configuration,
    parse_arguments,
    setup_logging,
    xplane_is_running,
)
from lib.settings import globals_list
from lib.touchosc import setup_touchosc_client, setup_touchosc_server
from lib.xplane import pull_xplane_data

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
    globals_list.current_version = CURRENT_VERSION
    globals_list.last_xplane_connection_ok = True
    globals_list.start_time = time.time()

    # Setup TouchOSC client
    client = setup_touchosc_client()
    globals_list.touchosc_client = client

    # Import modules of aircraft configuration
    load_aircraft_configuration()

    # Check if X-Plane is running and aircraft configuration is compatible with base script
    # if xplane_is_running() and aircraft_is_compatible():
    #     logger.info(f"Loading of {globals_list.args.aircraft} configuration successful.")

    # Let's start the show.
    asyncio.run(setup_loop())


async def loop():
    finished = False
    while not finished:
        # Enable time delay if X-Plane times out because of too many requests per second
        # time_delay = 0  # No time delay
        time_delay = 0.1  # No more than 10 requests per second
        # time_delay = 1  # No more than once per second, used for debug purposes

        if time.time() - globals_list.start_time > time_delay:
            pull_xplane_data()
            globals_list.start_time = time.time()

        await asyncio.sleep(0)


async def setup_loop():
    server = setup_touchosc_server()
    (
        transport,
        protocol,
    ) = (
        await server.create_serve_endpoint()
    )  # Create datagram endpoint and start serving

    await loop()  # Enter main loop of program

    transport.close()  # Clean up serve endpoint


if __name__ == "__main__":
    freeze_support()  # Pyinstaller needs this to support multiprocessing
    main()
