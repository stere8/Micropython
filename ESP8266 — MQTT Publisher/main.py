import network
import time
from umqtt.simple import MQTTClient

SSID = "YOUR_WIFI"
PASSWORD = "YOUR_PASSWORD"
BROKER_IP = "192.168.1.100"
TOPIC = b"class/display"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(1)

client = MQTTClient("esp8266_pub", BROKER_IP)
client.connect()

counter = 0
while True:
    msg = "Hello #" + str(counter)
    client.publish(TOPIC, msg)
    print("Sent:", msg)
    counter += 1
    time.sleep(5)
