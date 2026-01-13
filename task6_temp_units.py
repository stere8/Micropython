from machine import ADC
from utime import sleep
import ujson

temp_sensor = ADC(4)

while True:
    raw = temp_sensor.read_u16()
    voltage = raw * 3.3 / 65535
    c = 27 - (voltage - 0.706) / 0.001721
    k = c + 273.15
    f = c * 9 / 5 + 32

    payload = {
        "celsius": round(c, 2),
        "kelvin": round(k, 2),
        "fahrenheit": round(f, 2)
    }

    print(ujson.dumps(payload))
    sleep(2)
