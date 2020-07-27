import asyncio
import logging

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient

from lib.functions import globals_list

# Create a logger object
logger = logging.getLogger(__name__)


def __default_handler(address: str, *args) -> None:
    """Any unrecognized event that is sent by TouchOSC will be handled by the default_handler"""

    logger.warning(f"UNRECOGNIZED {address}: {args}")


def setup_touchosc_server() -> AsyncIOOSCUDPServer:
    """The OSC Server listens for events sent by an iPad or other device running TouchOSC.

    Returns:
        AsyncIOOSCUDPServer
    """

    dispatcher = Dispatcher()

    try:
        aircraft = globals_list.aircraft
        touchosc_list = aircraft.touchosc_address_dict.keys()
        for touchosc_address in touchosc_list:
            dispatcher.map(touchosc_address, __send_touchosc_result)
    except TypeError as e:
        logger.error(f"List with ToucOSC items is empty ({e}).")
    except AttributeError as e:
        logger.error(f"No controls were defined for TouchOSC ({e}).")

    dispatcher.set_default_handler(__default_handler)

    ip = globals_list.args.touchosc_server_ip
    port = int(globals_list.args.touchosc_server_port)
    logger.debug(f"Starting server on ip {ip} and port {port}")
    return AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())


def __send_touchosc_result(touchosc_address: str, *args) -> None:
    """Send the results we got from TouchOSC to the aircraft class for processing.

    Args:
        touchosc_address (str)
    """

    result = args[0]
    aircraft = globals_list.aircraft
    aircraft.process_touchosc_result(touchosc_address, result)


def setup_touchosc_client() -> SimpleUDPClient:
    """The touchOSC Client connects to an iPad or other device running TouchOSC

    Returns:
        SimpleUDPClient
    """

    logger.debug("Setting up TouchOSC client")
    ip = globals_list.args.touchosc_device_ip
    port = globals_list.args.touchosc_device_port

    return SimpleUDPClient(ip, port)  # Create client


def send_to_touchosc(touchosc_address: str, value) -> None:
    # Check for * in the address and remove it. A * is used by multi controls
    address = touchosc_address.replace("*", "")
    client = globals_list.touchosc_client
    logger.debug(client)

    try:
        client.send_message(address, value)
    except OSError as e:
        logger.error(f"Error when sending to value '{value}' to address {address} in TouchOSC ({e}).")
