import BlynkLib
import network
import time
from machine import Pin

led1=Pin(14,Pin.OUT)
led2=Pin(13,Pin.OUT)
led3=Pin(26,Pin.OUT)
 
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

 
@blynk.on("V1")
def v3_write_handler(value):
    if int(value[0])==1:
        led1.on()
    else:
      led1.off()
 
@blynk.on("V2")
def v2_write_handler(value):
    led2.value(int(value[0]))
    if int(value[0])==1:
        led2.on()
    else:
      led2.off()
      
@blynk.on("V3")
def v3_write_handler(value):
    led2.value(int(value[0]))
    if int(value[0])==1:
        led3.on()
    else:
      led3.off()
      
      
while True:
    blynk.run()
