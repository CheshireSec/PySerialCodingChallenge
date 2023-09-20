class SerialPort:
    def __init__(self, port_name, baud_rate=9600):
        """
        Initialize a SerialPort object.

        :param port_name: Name of the COM port, e.g. "COM1"
        :param baud_rate: Baud rate for the connection, default is 9600
        """
        self.name = port_name
        self.baud_rate = baud_rate

    def __str__(self):
        return f"SerialPort(name={self.name}, baud_rate={self.baud_rate})"
