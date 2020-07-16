import logging

# Create a logger object.
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

    @staticmethod
    def minimum_supported_version():
        return "0.0"

    @staticmethod
    def maximum_supported_version():
        return "0.0"

    @staticmethod
    def define_controls():
        # Return error if this method is not defined in child class
        logger.error("You haven't defined any controls.")

    # def reset_latest_xplane_result(self):
    #     self.latest_xplane_result.clear()

    def add_control(self, control):
        # TODO: Check for duplicates. Every control class should only be added once
        # Add control to X-Plane list if X-Plane drefs are defined
        if control.xplane_dref_address:
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
        # self.xplane_results = xplane_results
        # logger.debug("{}".format(xplane_results))

        # Trigger each control's callback
        for control in self.controls:
            control.callback_from_xplane(xplane_results)

    def process_touchosc_result(self, touchosc_address, touchosc_result):
        logger.debug(f"Processing result from TouchOSC: {touchosc_address} and value {touchosc_result}")
        # Get all elements of the address. Every TouchOCS address should be of format
        # /<category|tab>/<control_name>[/column/row]
        address_split = touchosc_address.split("/")
        if len(address_split) > 3:  # This is a multi control with column and row
            address = "/" + address_split[1] + "/" + address_split[2] + "*"
        else:
            address = touchosc_address

        control = self.touchosc_address_dict[address]
        # logger.debug(f"Handing over to control {control}")
        control.callback_from_touchosc(touchosc_address, touchosc_result)
