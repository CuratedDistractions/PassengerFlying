"""
Library to connect to X-Plane using NASA's X-Plane plugin.

Source: https://github.com/nasa/XPlaneConnect/blob/master/Python3/src/xpc.py
License: https://github.com/nasa/XPlaneConnect/blob/master/license.pdf

The sendCOMM method was added by Sander Datema (sander@curateddistractions.com)

"""

import socket
import struct


class XPlaneConnect:
    """XPlaneConnect (XPC) facilitates communication to and from the XPCPlugin."""

    socket = None

    # Basic Functions
    def __init__(self, xpHost="localhost", xpPort=49009, port=0, timeout=100):
        """Sets up a new connection to an X-Plane Connect plugin running in X-Plane.

            Args:
              xpHost: The hostname of the machine running X-Plane.
              xpPort: The port on which the XPC plugin is listening. Usually 49009.
              port: The port which will be used to send and receive data.
              timeout: The period (in milliseconds) after which read attempts will fail.
        """

        # Validate parameters
        xpIP = None
        try:
            xpIP = socket.gethostbyname(xpHost)
        # TODO: Make this 'except' more explicit
        except:
            raise ValueError("Unable to resolve xpHost.")

        if xpPort < 0 or xpPort > 65535:
            raise ValueError("The specified X-Plane port is not a valid port number.")
        if port < 0 or port > 65535:
            raise ValueError("The specified port is not a valid port number.")
        if timeout < 0:
            raise ValueError("Timeout must be non-negative.")

        # Setup XPlane IP and port
        self.xpDst = (xpIP, xpPort)

        # Create and bind socket
        clientAddr = ("0.0.0.0", port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket.bind(clientAddr)
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

    def sendUDP(self, buffer):
        """Sends a message over the underlying UDP socket."""
        # Preconditions
        if len(buffer) == 0:
            raise ValueError("sendUDP: buffer is empty.")

        self.socket.sendto(buffer, 0, self.xpDst)

    def readUDP(self):
        """Reads a message from the underlying UDP socket."""
        return self.socket.recv(16384)

    # DREF Manipulation
    def sendDREF(self, dref, values):
        """Sets the specified dataref to the specified value.
            Args:
              dref: The name of the datarefs to set.
              values: Either a scalar value or a sequence of values.
        """
        self.sendDREFs([dref], [values])

    def sendDREFs(self, drefs, values):
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
        self.sendUDP(buffer)

    def getDREF(self, dref):
        """Gets the value of an X-Plane dataref.
            Args:
              dref: The name of the dataref to get.
            Returns: A sequence of data representing the values of the requested dataref.
        """
        return self.getDREFs([dref])[0]

    def getDREFs(self, drefs):
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
        self.sendUDP(buffer)

        # Read and parse response
        buffer = self.readUDP()
        resultCount = struct.unpack_from(b"B", buffer, 5)[0]
        offset = 6
        result = []
        for i in range(resultCount):
            rowLen = struct.unpack_from(b"B", buffer, offset)[0]
            offset += 1
            fmt = "<{0:d}f".format(rowLen)
            row = struct.unpack_from(fmt.encode(), buffer, offset)
            result.append(row)
            offset += rowLen * 4
        return result

    def sendCOMM(self, comm):
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
        self.sendUDP(buffer)
