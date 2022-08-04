import BlynkLib
import network
import machine
import time
from machine import Pin

led1=Pin(14,Pin.OUT)

BLYNK_AUTH = "Here Your Blynk Authentication Token"


wifi = network.WLAN(network.STA_IF)
wifi.active(True)


while not wifi.isconnected():
    pass

print('IP:', wifi.ifconfig()[0])

blynk = BlynkLib.Blynk(BLYNK_AUTH)
tmr_start_time = time.time()

@blynk.on("connected")
def blynk_connected(ping,value):
    print("Connecting.................")
    print('Blynk ready. Ping:', ping, 'ms')
    print("Connected!")
    

@blynk.on("V1")
def v3_write_handler(value):
    if int(value[0])==1:
        led1.on()
    else:
      led1.off()

# Run blynk in the main thread:
while True:
    blynk.run()
