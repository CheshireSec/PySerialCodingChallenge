import serial
import serial.tools.list_ports
import threading
import time
import re
from SerialPort import SerialPort

# Stop event for shutting down the threads after Ctrl+C (KeyboardInterrupt)
stop_event = threading.Event()

# How often one port is writing to the other (in seconds)
write_interval = 5

def discover_com_ports():
    # Discovers and returns all available COM ports on the host system.
    return list(serial.tools.list_ports.comports())

def is_port_available(ports, port_name):
    # Check if a port name is available in the ports list
    for port in ports:
        if port.device == port_name:
            return True
    return False

def write_to_port(port: SerialPort, data):
    # Writes data to the specified COM port.
    with serial.Serial(port.name, port.baud_rate, timeout=1) as ser:
        while not stop_event.is_set():
            # Write to the serial port
            try:
                ser.write(data.encode('utf-8'))
                time.sleep(write_interval)
            except:
                break

def read_from_port(port: SerialPort):
    # Reads data from the specified COM port and prints it.
    with serial.Serial(port.name, port.baud_rate, timeout=1) as ser:
        while not stop_event.is_set():
            # Read from the serial port
            try:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    print(f"Received from {port.name}: {line}")
            except:
                break

def is_valid_com_port_name(port_name):
    # The pattern expects the string to start with "COM" followed by one or more digits
    pattern = r'^COM\d+$'
    return re.match(pattern, port_name) is not None

def main():
    # Discover available COM ports
    ports = discover_com_ports()
    
    # If no COM ports are available, gracefully fail
    if not ports:
        print("No COM ports available!")
        return

    # Print all available COM ports
    for port in ports:
        print(f"Available COM port: {port.device}")

    # Capturing the first COM port for connection
    first_com_port_name = input("Please enter the first COM port name (e.g. COM1): ")

    # If it's no valid COM port name (other than "COM..."), keep asking
    while not is_valid_com_port_name(first_com_port_name) or not is_port_available(ports, first_com_port_name):
        print(f"{first_com_port_name} is no available port name or no valid COM port name.")
        first_com_port_name = input("Please enter the first COM port name (e.g. COM1): ")
    
    # Capturing the first COM port for connection
    second_com_port_name = input("Please enter the first COM port name (e.g. COM2): ")

    # If it's no valid COM port name (other than "COM..."), keep asking
    while not is_valid_com_port_name(second_com_port_name) or not is_port_available(ports, second_com_port_name):
        print(f"{second_com_port_name} is no available port name or no valid COM port name.")
        second_com_port_name = input("Please enter the first COM port name (e.g. COM2): ")

    # Declare both SerialPorts and their baud rate
    first_com_port = SerialPort(first_com_port_name, 9600)
    second_com_port = SerialPort(second_com_port_name, 9600)

    # --- Proceed with threading, once the ports are captured, verified and initialized. ---

    message = input("Please enter the message, that should be sent from one COM port to the other: ")

    # Create a thread to write to the first COM port
    write_thread = threading.Thread(target=write_to_port, args=(first_com_port, message))
    
    # Create a thread to read from the second COM port
    read_thread = threading.Thread(target=read_from_port, args=(second_com_port,))

    # Start the threads
    write_thread.start()
    read_thread.start()

    print(f"Writing data to {first_com_port.name} and reading from {second_com_port.name}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:  # Catch Ctrl+C to gracefully shut down
        print("\nShutting down...")
        stop_event.set() 
        write_thread.join()
        read_thread.join()

if __name__ == "__main__":
    main()
