import logging

# Create a logger object
logger = logging.getLogger(__name__)


class BaseAircraft:
    def __init__(self):
        # Initialize some variables
        self.xplane_dref_address_list = []  # List of X-Plane drefs
        self.touchosc_address_dict = {}  # List of ToucOSC addresses
        self.controls = []  # List of all the controls
        # self.latest_xplane_result = {}  # Keeps track of previous results from X-Plane

        # Collect all controls. Each control will have some values declared and then it's
        # added to the aircraft using the add_control method.
        self.define_controls()

    def minimum_supported_version(self):
        return "0.0"

    def maximum_supported_version(self):
        return "0.0"

    @staticmethod
    def define_controls():
        # Return error if this method is not defined in child class
        logger.error("You haven't defined any controls.")

    def add_control(self, control):
        # Add control to X-Plane list if X-Plane drefs are defined
        if control.xplane_dref_address:
            # This is a simple duplicate check. For now we only accept a dref once
            if control.xplane_dref_address not in self.xplane_dref_address_list:
                self.xplane_dref_address_list.append(control.xplane_dref_address)

        # Add control to TouchOSC list if TouchOSC addresses are defined
        # This is a dict because we need to be able to find the control by
        # its touchosc_address
        if control.touchosc_address:
            if control.touchosc_address not in self.touchosc_address_dict:
                self.touchosc_address_dict[control.touchosc_address] = control

        self.controls.append(control)

    def process_xplane_result(self, xplane_results):
        # Trigger each control's callback
        for control in self.controls:
            control.callback_from_xplane(xplane_results)

    def process_touchosc_result(self, address, result):
        logger.debug(f"Processing result from TouchOSC: {address} and value {result}")

        # Get all elements of the address. Every TouchOCS address should be of format
        # /<category>/<control_name>[/column/row]
        address_split = address.split("/")
        if len(address_split) > 3:  # This is a multi control with column and row
            base_address = "/" + address_split[1] + "/" + address_split[2] + "*"
        else:
            base_address = address

        control = self.touchosc_address_dict[base_address]
        control.callback_from_touchosc(address, result)
