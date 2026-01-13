import serial
import time

# Find the correct COM port for your USB-to-TTL adapter (e.g., COM3 on Windows, /dev/ttyUSB0 on Linux)
# Check Device Manager (Windows) or terminal (Linux: ls /dev/tty*)
port = 'COM6' # <--- CHANGE THIS TO YOUR PORT
baud_rate = 9600

try:
    ser = serial.Serial(port, baud_rate, timeout=1)
    print(f"Connected to {port}")
    time.sleep(2) # Wait for connection to establish

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(f"Received: {line}")
except serial.SerialException as e:
    print(f"Error connecting to serial port: {e}")
    print("Please check your port and connection.")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed.")