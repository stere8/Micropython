from machine import ADC
from utime import sleep

joy_x = ADC(26)   # VRx
joy_y = ADC(27)   # VRy

while True:
    print("X position =", joy_x.read_u16())
    print("Y position =", joy_y.read_u16())
    print("----------------------")
    sleep(0.5)
     