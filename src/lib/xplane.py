import logging
import socket
import struct

from lib.settings import globals_list

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
                yield lst[i: i + n]

        for batch in chunks(xplane_dref_address_list, batch_size):
            result.extend(xplane_client.get_drefs(batch))

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
        xplane_client.send_dref(dref, value)
    else:
        xplane_client.send_comm(dref)
    xplane_client.close()


def get_from_xplane(dref):
    xplane_client = XPlaneConnect()
    result = xplane_client.get_dref(dref)
    xplane_client.close()
    return result


def __reassign_results_to_drefs(results, xplane_dref_address_list):
    list_with_drefs_and_results = {}
    for idx, result in enumerate(results):
        dref = xplane_dref_address_list[idx]  # Match result with dref with same index
        list_with_drefs_and_results[dref] = result

    return list_with_drefs_and_results


class XPlaneConnect:
    """XPlaneConnect (XPC) facilitates communication to and from the XPCPlugin.

    Library to connect to X-Plane using NASA's X-Plane plugin.

    Source: https://github.com/nasa/XPlaneConnect/blob/master/Python3/src/xpc.py
    License: https://github.com/nasa/XPlaneConnect/blob/master/license.pdf

    The send_comm method was added by Sander Datema (sander@curateddistractions.com)
    """

    socket = None

    # Basic Functions
    def __init__(self, xp_host="localhost", xp_port=49009, port=0, timeout=100):
        """Sets up a new connection to an X-Plane Connect plugin running in X-Plane.

            Args:
              xp_host: The hostname of the machine running X-Plane.
              xp_port: The port on which the XPC plugin is listening. Usually 49009.
              port: The port which will be used to send and receive data.
              timeout: The period (in milliseconds) after which read attempts will fail.
        """

        # Validate parameters
        xp_ip = None
        try:
            xp_ip = socket.gethostbyname(xp_host)
        # TODO: Make this 'except' more explicit
        except:
            raise ValueError("Unable to resolve xp_host.")

        if xp_port < 0 or xp_port > 65535:
            raise ValueError("The specified X-Plane port is not a valid port number.")
        if port < 0 or port > 65535:
            raise ValueError("The specified port is not a valid port number.")
        if timeout < 0:
            raise ValueError("Timeout must be non-negative.")

        # Setup XPlane IP and port
        self.xp_dst = (xp_ip, xp_port)

        # Create and bind socket
        client_addr = ("0.0.0.0", port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.bind(client_addr)
        timeout /= 1000.0
        self.socket.settimeout(timeout)

    def __del__(self):
        self.close()

    # Define __enter__ and __exit__ to support the `with` construct.
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        """Closes the specified connection and releases resources associated with it."""
        if self.socket is not None:
            self.socket.close()
            self.socket = None

    def send_udp(self, buffer):
        """Sends a message over the underlying UDP socket."""
        # Preconditions
        if len(buffer) == 0:
            raise ValueError("send_udp: buffer is empty.")

        self.socket.sendto(buffer, 0, self.xp_dst)

    def read_udp(self):
        """Reads a message from the underlying UDP socket."""
        return self.socket.recv(16384)

    # DREF Manipulation
    def send_dref(self, dref, values):
        """Sets the specified dataref to the specified value.
            Args:
              dref: The name of the datarefs to set.
              values: Either a scalar value or a sequence of values.
        """
        self.send_drefs([dref], [values])

    def send_drefs(self, drefs, values):
        """Sets the specified datarefs to the specified values.
            Args:
              drefs: A list of names of the datarefs to set.
              values: A list of scalar or vector values to set.
        """
        if len(drefs) != len(values):
            raise ValueError("drefs and values must have the same number of elements.")

        buffer = struct.pack(b"<4sx", b"DREF")
        for i in range(len(drefs)):
            dref = drefs[i]
            value = values[i]

            # Preconditions
            if len(dref) == 0 or len(dref) > 255:
                raise ValueError("dref must be a non-empty string less than 256 characters.")

            if value is None:
                raise ValueError("value must be a scalar or sequence of floats.")

            # Pack message
            if hasattr(value, "__len__"):
                if len(value) > 255:
                    raise ValueError("value must have less than 256 items.")
                fmt = "<B{0:d}sB{1:d}f".format(len(dref), len(value))
                buffer += struct.pack(fmt.encode(), len(dref), dref.encode(), len(value), *value)
            else:
                fmt = "<B{0:d}sBf".format(len(dref))
                buffer += struct.pack(fmt.encode(), len(dref), dref.encode(), 1, value)

        # Send
        self.send_udp(buffer)

    def get_dref(self, dref):
        """Gets the value of an X-Plane dataref.
            Args:
              dref: The name of the dataref to get.
            Returns: A sequence of data representing the values of the requested dataref.
        """
        return self.get_drefs([dref])[0]

    def get_drefs(self, drefs):
        """Gets the value of one or more X-Plane datarefs.
            Args:
              drefs: The names of the datarefs to get.
            Returns: A multidimensional sequence of data representing the values of the requested
             datarefs.
        """
        # Send request
        buffer = struct.pack(b"<4sxB", b"GETD", len(drefs))
        for dref in drefs:
            fmt = "<B{0:d}s".format(len(dref))
            buffer += struct.pack(fmt.encode(), len(dref), dref.encode())
        self.send_udp(buffer)

        # Read and parse response
        buffer = self.read_udp()
        result_count = struct.unpack_from(b"B", buffer, 5)[0]
        offset = 6
        result = []
        for _ in range(result_count):
            row_len = struct.unpack_from(b"B", buffer, offset)[0]
            offset += 1
            fmt = "<{0:d}f".format(row_len)
            row = struct.unpack_from(fmt.encode(), buffer, offset)
            result.append(row)
            offset += row_len * 4
        return result

    def send_comm(self, comm):
        """Sends the specified command.

            Args:
            comm: dref of the command.
        """
        if comm is None:
            raise ValueError("comm must be non-empty.")

        buffer = struct.pack(b"<4sx", b"COMM")
        if len(comm) == 0 or len(comm) > 255:
            raise ValueError("comm must be a non-empty string less than 256 characters.")

        # Pack message
        fmt = "<B{0:d}s".format(len(comm))
        buffer += struct.pack(fmt, len(comm), comm.encode())

        # Send
        self.send_udp(buffer)
