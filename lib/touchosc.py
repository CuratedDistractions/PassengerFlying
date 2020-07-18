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
            # logger.debug(aircraft.__dict__)
            aircraft = settings.globalList["AIRCRAFT"]
            touchosc_list = aircraft.touchosc_address_dict.keys()
            # logger.debug("touchOSC list: {}".format(touchosc_list.keys()))
            for touchosc_address in touchosc_list:
                # logger.debug(f"dispatcher.map({touchosc_address}), send_touchosc_result")

                # TODO: Check if last argument for the dispatcher is still needed.
                dispatcher.map(touchosc_address, self.send_touchosc_result, aircraft)
        except TypeError as e:
            logger.error(f"List with touchosc items is empty ({e}).")
        except AttributeError as e:
            logger.error(f"No controls were defined for TouchOSC ({e}).")

        dispatcher.set_default_handler(self.__default_handler)

        if self.args.touchosc_server_ip is None:
            ip = "127.0.0.1"
        else:
            ip = self.args.touchosc_device_ip

        if self.args.touchosc_server_port is None:
            port = 5006
        else:
            port = self.args.touchosc_server_port

        try:
            server = BlockingOSCUDPServer((ip, port), dispatcher)
            server.serve_forever()
        except OSError as e:
            logger.error(f"Can't start touchOSC server ({e}).")

    def send_touchosc_result(self, touchosc_address, *args):
        logger.debug("Processing send_touchosc_result {}".format(args))
        aircraft = args[0][0]
        result = args[1]
        aircraft.process_touchosc_result(touchosc_address, result)

    def client(self):
        """The touchOSC Client connects to an iPad or other device running TouchOSC"""

        # IP address and port of TouchOSC device
        ip = self.args.touchosc_device_ip
        if self.args.touchosc_device_port is None:
            port = 5005
        else:
            port = self.args.touchosc_server_port

        # TODO: Try/Except
        return SimpleUDPClient(ip, port)  # Create client

    def send_to_touchosc(self, touchosc_address, value):
        # Check for * in the address and remove it. A * is used by multi controls
        address = touchosc_address.replace("*", "")
        # logger.debug("Sending command to TouchOSC: {} {}".format(address, value))
        self.touchosc_client.send_message(address, value)
