import logging
import socket

from lib.settings import globals_list
from lib.nasa_xpc import XPlaneConnect

# Create a logger object
logger = logging.getLogger(__name__)


def pull_xplane_data():
    """This functions connects to NASA's X-plane Connector through their Python XPC library.

    It needs to actively poll for information, which is not ideal. Right now the script polls about
    10 times per second.
    In the future I'd like dref changed from X-Plane be pushed. But I'll need to wait till Python 3 is available
    as an X-Plane plugin. It's being worked on, so we'll see.
    """
    aircraft = globals_list.aircraft

    # Fetch all registered drefs in one bundle
    xplane_dref_address_list = aircraft.xplane_dref_address_list

    try:
        xplane_client = XPlaneConnect()

        # X-Plane might crash if we request to many drefs at once. So we'll cut the list in
        # smaller batches.
        # TODO: Get size of X-Plane arrays and sort batches evenly
        result = []
        batch_size = 20

        def chunks(lst, n):
            """Yield successive n-sized chunks from lst.

            Credits: https://stackoverflow.com/a/312464/776118
            """
            for i in range(0, len(lst), n):
                yield lst[i : i + n]

        for batch in chunks(xplane_dref_address_list, batch_size):
            result.extend(xplane_client.getDREFs(batch))

        if globals_list.last_xplane_connection_ok is False:
            logger.warning("Connection restored!")
        xplane_client.close()
        globals_list.last_xplane_connection_ok = True  # Success, we didn't time out
    except socket.timeout as e:
        if globals_list.last_xplane_connection_ok:  # It's no longer ok
            logger.warning(f"Lost connection with X-Plane ({e}). Not a problem, will try again.")
        globals_list.last_xplane_connection_ok = False

    if globals_list.last_xplane_connection_ok:
        # Return the values to the aircraft configuration

        # Add the original dref addresses to the returned values
        list_with_drefs_and_results = __reassign_results_to_drefs(result, xplane_dref_address_list)

        # And return the results to the aircraft configuration
        aircraft.process_xplane_result(list_with_drefs_and_results)


def send_to_xplane(dref, value=None):
    xplane_client = XPlaneConnect()
    if value is not None:
        xplane_client.sendDREF(dref, value)
    else:
        xplane_client.sendCOMM(dref)
    xplane_client.close()


def get_from_xplane(dref):
    xplane_client = XPlaneConnect()
    result = xplane_client.getDREF(dref)
    xplane_client.close()
    return result


def __reassign_results_to_drefs(results, xplane_dref_address_list):
    list_with_drefs_and_results = {}
    for idx, result in enumerate(results):
        dref = xplane_dref_address_list[idx]  # Match result with dref with same index
        list_with_drefs_and_results[dref] = result

    return list_with_drefs_and_results
