import logging

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient

import lib.settings as settings

# Create a logger object.
logger = logging.getLogger(__name__)


class TouchOSC:
    def __init__(self):
        self.args = settings.globalList["ARGS"]
        self.client = self.__setup_client()

    @staticmethod
    def __default_handler(address, *args):
        """Any unrecognized event that is sent by TouchOSC will be handled by the default_handler"""

        logger.warning(f"UNRECOGNIZED {address}: {args}")

    def server(self):
        """The OSC Server listens for events sent by an iPad or other device running TouchOSC

        As this is a blocking function, the main() function will use Process to run it alongside
        any other processes.
        """

        dispatcher = Dispatcher()

        try:
            aircraft = settings.globalList["AIRCRAFT"]
            touchosc_list = aircraft.touchosc_address_dict.keys()
            for touchosc_address in touchosc_list:
                # TODO: Check if last argument for the dispatcher is still needed.
                dispatcher.map(touchosc_address, self.send_touchosc_result, aircraft)
        except TypeError as e:
            logger.error(f"List with touchosc items is empty ({e}).")
        except AttributeError as e:
            logger.error(f"No controls were defined for TouchOSC ({e}).")

        dispatcher.set_default_handler(self.__default_handler)

        ip = self.args.touchosc_server_ip
        port = int(self.args.touchosc_server_port)

        try:
            server = BlockingOSCUDPServer((ip, port), dispatcher)
            server.serve_forever()
        except OSError as e:
            logger.error(f"Can't start touchOSC server ({e}).")

    def send_touchosc_result(self, touchosc_address, *args):
        aircraft = args[0][0]
        result = args[1]
        aircraft.process_touchosc_result(touchosc_address, result)

    def __setup_client(self):
        """The touchOSC Client connects to an iPad or other device running TouchOSC"""

        # IP address and port of TouchOSC device
        ip = self.args.touchosc_device_ip
        port = int(self.args.touchosc_device_port)

        return SimpleUDPClient(ip, port)  # Create client

    def send_to_touchosc(self, touchosc_address, value):
        # Check for * in the address and remove it. A * is used by multi controls
        address = touchosc_address.replace("*", "")
        try:
            self.client.send_message(address, value)
        except OSError as e:
            logger.error(f"Error when sending to value '{value}' to address {address} in TouchOSC ({e}).")
