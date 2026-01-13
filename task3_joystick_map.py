from machine import ADC
from utime import sleep

def analog_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) /
               (in_max - in_min) + out_min)

joy_x = ADC(26)
joy_y = ADC(27)  

while True:
    valuex = analog_map(joy_x.read_u16(), 0, 65535, -10, 10)
    valuey = analog_map(joy_y.read_u16(), 0, 65535, -10, 10)
    print(f"X: {valuex}, Y: {valuey}")
    sleep(1)
