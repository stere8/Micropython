from machine import Pin, UART,ADC
from utime import sleep
import ujson

uart = UART(0, baudrate=115200)


def analog_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) /
               (in_max - in_min) + out_min)

joy_x = ADC(26)
joy_y = ADC(27)

temp_sensor = ADC(4)


while True:
    raw = temp_sensor.read_u16()
    voltage = raw * 3.3 / 65535
    temperature = 27 - (voltage - 0.706) / 0.001721
    valuex = analog_map(joy_x.read_u16(), 0, 65535, 0, 10)
    valuey = analog_map(joy_y.read_u16(), 0, 65535, 0, 10)
    print(f"X: {valuex}, Y: {valuey}")
    payload = {
        "joystick": {
            "x": valuex,
            "y": valuey
        },
        "climate":{
            "temperature" : temperature}
    }
    sleep(1)
    uart.write(ujson.dumps(payload) + "\n")
    uart.write("message sent")
    print("Sent" +ujson.dumps(payload) + "\n")
    sleep(1)
    