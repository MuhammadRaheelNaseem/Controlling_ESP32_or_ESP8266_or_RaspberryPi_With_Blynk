from time import sleep
from hcsr04 import HCSR04
import dht
from machine import Pin
import BlynkLib
import network
import machine
import time
from machine import Pin
import dht

sensor = HCSR04(trigger_pin=26, echo_pin=27, echo_timeout_us=10000)

BLYNK_AUTH = 'Here Your Blynk Authentication Token'


wifi = network.WLAN(network.STA_IF)
wifi.active(True)


while not wifi.isconnected():
    pass

print('IP:', wifi.ifconfig()[0])

blynk = BlynkLib.Blynk(BLYNK_AUTH)
tmr_start_time = time.time()

@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')
    print("Connected!")
    while True:
        distance = sensor.distance_cm()
        print('Distance:', distance, 'cm')
        blynk.virtual_write("20",distance)
        sleep(1)

# Run blynk in the main thread:
while True:
    blynk.run()
