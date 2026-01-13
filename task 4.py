from machine import Pin, UART
from utime import sleep

uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart1.init(bits=8, parity=None, stop=1)

led = Pin('LED', Pin.OUT)

while True:
    uart1.write("a" + "\n")
    if uart1.any():
        char = uart1.read()
        if char == b'x':
            led.toggle()
    sleep(0.5)
