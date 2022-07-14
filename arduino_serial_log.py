import time
from os.path import isfile
import serial  # this requires that you have installed the pyserial module with pip install

port_name = '/dev/cu.usbserial-A6008iRf'  # Arduino's USB port, either COMxx for PC or /dev/cu.usb-serial-xxxxxx for Mac
baud_rate = 9600  # baudrate should be equivalent to that used in Arduino sketch (e.g. 9600)
sample_rate = 1  # number of seconds between samples (this should be equivalent to any delay in the sketch)
arduino = serial.Serial(port=port_name, baudrate=baud_rate, timeout=sample_rate*1.2)

file_name = input("Enter file name (.csv will be appended automatically): ")
if "csv" not in file_name:
    file_name += ".csv"

if not isfile(file_name):
    with open(file_name, "a+") as file:
        # creates handle for chosen filename. Use of "+" ensures file
        # will be created if it doesn't exist
        file.write("Time,Temperature,Humidity" + "\n")
        # writes data headers surrounded by newlines (use of "a" in file
        # handle above ensures data is appended, rather than overwriting)

while True:
    # creates infinite loop
    arduino_data = arduino.readline().strip()
    arduino_data = str(arduino_data, 'utf-8')
    # creates float out of most recent line of serial data,
    # striping newline etc
    print(arduino_data)

    with open(file_name, "a") as file:
        file.write(time.strftime("%Y-%m-%d %H:%M:%S") + ", " + str(arduino_data) + "\n")
