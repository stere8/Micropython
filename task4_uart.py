from machine import UART
import time
import ujson

# Initialize UART on GP4 (TX) and GP5 (RX) at 115200 baud
uart = UART(0, baudrate=115200)



payload = {
    "command": "start",
    "value": 10
}


print("Pico Serial Sender Started!")
content = ujson.dumps(payload) + "\n"
while True:
    # Send a simple message every second
    message = content
    uart.write(message)
    print(f"Sent: {message.strip()}")
    time.sleep(1)
