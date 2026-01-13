from machine import ADC
from utime import sleep

# Internal temperature sensor = ADC channel 4
temp_sensor = ADC(4)

while True:
    raw = temp_sensor.read_u16()
    voltage = raw * 3.3 / 65535
    temperature = 27 - (voltage - 0.706) / 0.001721

    print("Temperature: {:.2f} °C".format(temperature))
    sleep(2)
