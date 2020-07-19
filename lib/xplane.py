import logging
import socket
import time

import lib.settings as settings
from lib.nasa_xpc import XPlaneConnect

# Create a logger object.
logger = logging.getLogger(__name__)


# XPC client
# TODO: close connection when done


class XPlane:
    def xplane_monitor(self):
        """This functions connects to NASA's X-plane Connector through their Python XPC library.

        It needs to actively poll for information, which is not ideal. Right now the script polls about
        10 times per second.
        In the future I'd like dref changed from X-Plane be pushed. But I'll need to wait till Python 3 is available
        as an X-Plane plugin. It's being worked on, so we'll see.
        """

        aircraft = settings.globalList["AIRCRAFT"]

        # Fetch all registered drefs in one bundle
        xplane_dref_address_list = aircraft.xplane_dref_address_list

        # Track if connection with X-Plane timed out
        last_connection_ok = True

        while True:
            # Enable time delay if X-Plane times out because of too many requests per second
            time_delay = True
            time_delay_amount = 0.1  # No more than 10 requests per second
            # time_delay_amount = 1  # No more than once per second, used for debug purposes

            if time_delay:
                time_start = time.time()  # Save timestamp, so we can decide if we need to pause at the end of this loop

            try:
                xplane_client = XPlaneConnect()
                # logger.debug("List to check: {}".format(xplane_dref_address_list))
                result = xplane_client.getDREFs(xplane_dref_address_list)
                if last_connection_ok is False:
                    logger.info("Connection restored!")
                xplane_client.close()
                last_connection_ok = True  # Success, we didn't time out
            except socket.timeout as e:
                # aircraft.reset_latest_xplane_result()
                if last_connection_ok:  # It's no longer ok
                    logger.warning(f"Lost connection with X-Plane ({e}). Not a problem, will try again.")
                last_connection_ok = False

            if last_connection_ok:
                # Return the values to the aircraft configuration

                # Add the original dref addresses to the returned values
                list_with_drefs_and_results = self.reassign_results_to_drefs(result, xplane_dref_address_list)
                # logger.debug(
                #     "List with results: {}".format(list_with_drefs_and_results)
                # )

                # And return the results to the aircraft configuration
                aircraft.process_xplane_result(list_with_drefs_and_results)

            if time_delay:  # See top of method for explanation
                time_taken = time.time() - time_start
                if time_taken < time_delay_amount:
                    time.sleep(time_delay_amount - time_taken)

    def send_to_xplane(self, dref, value=None):
        xplane_client = XPlaneConnect()
        if value:
            xplane_client.sendDREF(dref, value)
        else:
            xplane_client.sendCOMM(dref)
        xplane_client.close()

    def get_from_xplane(self, dref):
        xplane_client = XPlaneConnect()
        result = xplane_client.getDREF(dref)
        xplane_client.close()
        return result

    def reassign_results_to_drefs(self, results, xplane_dref_address_list):
        list_with_drefs_and_results = {}
        for idx, result in enumerate(results):
            dref = xplane_dref_address_list[idx]  # Match result with dref with same index
            list_with_drefs_and_results[dref] = result

        return list_with_drefs_and_results
