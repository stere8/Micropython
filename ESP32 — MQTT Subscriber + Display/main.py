import network
import time
from machine import Pin, SPI
from umqtt.simple import MQTTClient
import ili9341

SSID = "YOUR_WIFI"
PASSWORD = "YOUR_PASSWORD"
BROKER_IP = "192.168.1.100"
TOPIC = b"class/display"

spi = SPI(1, baudrate=40000000, sck=Pin(18), mosi=Pin(23))
display = ili9341.Display(spi, dc=Pin(2), cs=Pin(5), rst=Pin(4))

display.clear()
display.draw_text(10, 10, "Waiting for MQTT...", ili9341.color565(255,255,255))

def on_msg(topic, msg):
    display.clear()
    display.draw_text(10, 10, "Message:", ili9341.color565(0,255,0))
    display.draw_text(10, 50, msg.decode(), ili9341.color565(255,255,0))

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(1)

client = MQTTClient("esp32_sub", BROKER_IP)
client.set_callback(on_msg)
client.connect()
client.subscribe(TOPIC)

while True:
    client.check_msg()
    time.sleep(0.1)
