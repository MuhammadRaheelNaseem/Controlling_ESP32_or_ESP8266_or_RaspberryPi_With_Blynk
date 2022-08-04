</pre>
from time import sleep
import dht
from machine import Pin
import BlynkLib
import network
import machine
import time
from machine import Pin
import dht

sensor = dht.DHT11(Pin(33))

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
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print('Air Temperature: %3.1f C' %temp)
        print('Air Humidity: %3.1f %%' %hum)
        blynk.virtual_write('13',temp)
        blynk.virtual_write('14',hum)
        sleep(1)

# Run blynk in the main thread:
while True:
    blynk.run()
