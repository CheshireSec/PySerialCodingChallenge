# PySerial COM Port Coding Challenge

This Python script allows communication between two COM ports (COM port pair) using the pySerial library. It is designed to work with virtual COM ports simulated by the Com0Com Virtual COM Port Emulator on Windows.

## Prerequisites

- Python 3.x
- Com0Com Virtual COM Port Emulator

## Setting Up

### Installing Com0Com

1. Download and install the Com0Com Virtual COM Port Emulator from the official SourceForge repository.
2. During installation, when prompted, trust the driver by accepting the pop-up.
3. Start the Com0Com application by starting the "setupg.exe" file in the root directory of the program.

### Setting Up The Python Environment

1. Navigate to the root project directory in your terminal or command prompt.

2. Set up a virtual environment:

   ```bash
   py -m venv env
   ```

3. Activate the virtual environment:

   ```bash
   .\env\Scripts\activate
   ```

   Note: Your prompt should now be prefixed with `(env)` indicating the virtual environment is active.

4. Install the required Python libraries:

   ```bash
   py -m pip install -r requirements.txt
   ```

## Running the Script

1. Ensure the virtual environment is active. If not, activate it using:

   ```bash
   .\env\Scripts\activate
   ```

2. Run the main script:

   ```bash
   py .\main.py
   ```

3. Follow the on-screen prompts to select the COM ports for communication and the message that should be sent.

## Sample Output

```
(env) PS C:\Users\UserXXX\Dev\PySerialChallenge> py .\main.py
Available COM port: COM1
Available COM port: COM5
Available COM port: COM6
Available COM port: COM4
Available COM port: COM7
Please enter the first COM port name (e.g. COM1): COM6 
Please enter the first COM port name (e.g. COM2): COM7
Please enter the message, that should be sent from one COM port to the other: Hello from COM6 to COM7! 
Writing data to COM6 and reading from COM7...
Received from COM7: Hello from COM6 to COM7!
{Ctrl-C KeyboardInterrupt}

Shutting down...
(env) PS C:\Users\UserXXX\Dev\PySerialChallenge> 
```
