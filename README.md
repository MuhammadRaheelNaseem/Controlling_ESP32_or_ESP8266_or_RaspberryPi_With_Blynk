# Controlling_ESP32_or_ESP8266_With_Blynk
<header>
    <p style="justify:center;">
        Design By Muhammad Raheel
    </p>
</header>

# `Step 1:  Create Blynk Cloud FREE Account`

Click on the following link to create a Blynk Cloud account.

https://blynk.cloud/dashboard/register

1. Enter email ID, then click on "Sign Up". You will receive a verification email.
2. Click on Create Password in the email, Then set the password, click on Next.
3. Enter your first name, click on Done.

After that Blynk cloud dashboard will open.

![image](https://user-images.githubusercontent.com/63813881/182760742-e40b4380-0d7a-4c46-9786-42918fab1235.png)


`after signup confirm email then enter password`

![image](https://user-images.githubusercontent.com/63813881/182760776-e8eead4b-f47d-4ba2-a98e-08d0c2461540.png)

`then enter password`

![image](https://user-images.githubusercontent.com/63813881/182760802-3d112063-ddaa-4bdf-a1aa-a395c311c326.png)

`then enter profile name`

![image](https://user-images.githubusercontent.com/63813881/182760825-57f2864f-2c79-4d54-9475-d3894f3adb15.png)

`if you see this then skip this process`

![image](https://user-images.githubusercontent.com/63813881/182760861-58f8bd70-3d26-464a-8e17-bf0d8a5dca45.png)

`Click Cancel Button`

![image](https://user-images.githubusercontent.com/63813881/182760890-ba4f4cc2-5bd8-4899-98d8-a8d206f7b177.png)

# `Step 2: Create a New Template in Blynk Cloud`

First, you have to create a template in the Blynk cloud.

1. Click on New Template.
2. Enter a template name, select the hardware as ESP8266, and the connection type will WiFi.
3. Then click on DONE.

You will get the BLYNK_TEMPLATE_ID and BLYNK_DEVICE_NAME after creating the temple.

![image](https://user-images.githubusercontent.com/63813881/182760932-71dd5fd2-70db-4d3c-a587-b4e5c0acdd33.png)
![image](https://user-images.githubusercontent.com/63813881/182760955-5d52796b-bfe4-4e1a-b795-e7eb9da89dc7.png)
![image](https://user-images.githubusercontent.com/63813881/182760967-475adbda-fcab-46b5-b9a5-5a18dff97265.png)

# `Step 3: Create a New Device in Blynk Cloud`

![image](https://user-images.githubusercontent.com/63813881/182760985-d0e8f18b-942b-4e69-adf2-ddc81a9b8b5c.png)

`Click New Device`

![image](https://user-images.githubusercontent.com/63813881/182761000-663b9c1f-9e68-49ef-96ea-2e1866045c29.png)

`Click Here for template`

![image](https://user-images.githubusercontent.com/63813881/182761024-0f5c5afb-a061-4dd3-9042-ef27bfd8d17d.png)
![image](https://user-images.githubusercontent.com/63813881/182761059-9eac0327-a2d9-4904-9689-f8ee698715d5.png)
![image](https://user-images.githubusercontent.com/63813881/182761085-a05ffaab-21f0-42b3-9a8b-645f8df600ac.png)

`You will get things`

![image](https://user-images.githubusercontent.com/63813881/182761108-d0402c5f-fbe9-4085-9bdd-8da692037588.png)

`Click Device Info`

![image](https://user-images.githubusercontent.com/63813881/182761135-2ca6f97e-b093-4e11-b1f1-c35d7b0060c7.png)

`After click you will get Device Auth key`

![image](https://user-images.githubusercontent.com/63813881/182761158-e996c5c7-27fd-47c8-b9b2-38bad5105176.png)

![image](https://user-images.githubusercontent.com/63813881/182761189-e5c40181-29fc-4890-820c-034216518635.png)
![image](https://user-images.githubusercontent.com/63813881/182761218-3f314e5d-f227-4eaf-93f3-18cf474e17b5.png)

![image](https://user-images.githubusercontent.com/63813881/182761241-4434f895-fe4e-4af6-9818-dcd84682091e.png)
![image](https://user-images.githubusercontent.com/63813881/182761262-b86fb9f4-629b-4111-bad7-f508585d1af9.png)
![image](https://user-images.githubusercontent.com/63813881/182761276-a8297f31-ab9b-4863-a79c-1d8912351538.png)
![image](https://user-images.githubusercontent.com/63813881/182761305-721daccd-0eb7-4c1d-868e-d8cc407e2010.png)
![image](https://user-images.githubusercontent.com/63813881/182761321-6d961a51-bf68-424a-8f1f-ad9cc71a5f40.png)
![image](https://user-images.githubusercontent.com/63813881/182761524-f66e11e7-c8e4-4b65-b734-11069722fc2b.png)
![image](https://user-images.githubusercontent.com/63813881/182761497-e80b56bd-116b-4c92-8825-1a625ae74999.png)
![image](https://user-images.githubusercontent.com/63813881/182761436-06b1188f-5af7-4b48-9d7a-529a445b2493.png)
![image](https://user-images.githubusercontent.com/63813881/182761418-5f6cb72a-29b6-4e42-8150-590184a13bcb.png)
![image](https://user-images.githubusercontent.com/63813881/182761384-1c480f4d-ede0-4210-8ffd-1737fb543254.png)
![image](https://user-images.githubusercontent.com/63813881/182761360-54507ad6-3224-4104-b465-40339806610b.png)



# `boot.py`
<pre>
import network
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        print(sta_if.scan())
        sta_if.connect("wifi Router SSID", "Wifi Router Password")
        sta_if.connect("IoT_Device",'Thejudgementday@')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()
</pre>

### `This is the library of blynk which help you to connect with blynk app or blynk cloud platform`
# `BlynkLib.py`
<pre>

# Copyright (c) 2015-2019 Volodymyr Shymanskyy. See the file LICENSE for copying permission.

__version__ = "1.0.0"

import struct
import time
import sys
import os

try:
    import machine
    gettime = lambda: time.ticks_ms()
    SOCK_TIMEOUT = 0
except ImportError:
    const = lambda x: x
    gettime = lambda: int(time.time() * 1000)
    SOCK_TIMEOUT = 0.05

def dummy(*args):
    pass

MSG_RSP = const(0)
MSG_LOGIN = const(2)
MSG_PING  = const(6)

MSG_TWEET = const(12)
MSG_NOTIFY = const(14)
MSG_BRIDGE = const(15)
MSG_HW_SYNC = const(16)
MSG_INTERNAL = const(17)
MSG_PROPERTY = const(19)
MSG_HW = const(20)
MSG_HW_LOGIN = const(29)
MSG_EVENT_LOG = const(64)

MSG_REDIRECT  = const(41)  # TODO: not implemented
MSG_DBG_PRINT  = const(55) # TODO: not implemented

STA_SUCCESS = const(200)
STA_INVALID_TOKEN = const(9)

DISCONNECTED = const(0)
CONNECTING = const(1)
CONNECTED = const(2)

print("""
    ___  __          __
   / _ )/ /_ _____  / /__
  / _  / / // / _ \\/  '_/
 /____/_/\\_, /_//_/_/\\_\\
        /___/ for Python v""" + __version__ + " (" + sys.platform + ")\n")

class EventEmitter:
    def __init__(self):
        self._cbks = {}

    def on(self, evt, f=None):
        if f:
            self._cbks[evt] = f
        else:
            def D(f):
                self._cbks[evt] = f
                return f
            return D

    def emit(self, evt, *a, **kv):
        if evt in self._cbks:
            self._cbks[evt](*a, **kv)


class BlynkProtocol(EventEmitter):
    def __init__(self, auth, tmpl_id=None, fw_ver=None, heartbeat=50, buffin=1024, log=None):
        EventEmitter.__init__(self)
        self.heartbeat = heartbeat*1000
        self.buffin = buffin
        self.log = log or dummy
        self.auth = auth
        self.tmpl_id = tmpl_id
        self.fw_ver = fw_ver
        self.state = DISCONNECTED
        self.connect()

    def virtual_write(self, pin, *val):
        self._send(MSG_HW, 'vw', pin, *val)

    def send_internal(self, pin, *val):
        self._send(MSG_INTERNAL,  pin, *val)

    def set_property(self, pin, prop, *val):
        self._send(MSG_PROPERTY, pin, prop, *val)

    def sync_virtual(self, *pins):
        self._send(MSG_HW_SYNC, 'vr', *pins)

    def log_event(self, *val):
        self._send(MSG_EVENT_LOG, *val)

    def _send(self, cmd, *args, **kwargs):
        if 'id' in kwargs:
            id = kwargs.get('id')
        else:
            id = self.msg_id
            self.msg_id += 1
            if self.msg_id > 0xFFFF:
                self.msg_id = 1
                
        if cmd == MSG_RSP:
            data = b''
            dlen = args[0]
        else:
            data = ('\0'.join(map(str, args))).encode('utf8')
            dlen = len(data)
        
        self.log('<', cmd, id, '|', *args)
        msg = struct.pack("!BHH", cmd, id, dlen) + data
        self.lastSend = gettime()
        self._write(msg)

    def connect(self):
        if self.state != DISCONNECTED: return
        self.msg_id = 1
        (self.lastRecv, self.lastSend, self.lastPing) = (gettime(), 0, 0)
        self.bin = b""
        self.state = CONNECTING
        self._send(MSG_HW_LOGIN, self.auth)

    def disconnect(self):
        if self.state == DISCONNECTED: return
        self.bin = b""
        self.state = DISCONNECTED
        self.emit('disconnected')

    def process(self, data=None):
        if not (self.state == CONNECTING or self.state == CONNECTED): return
        now = gettime()
        if now - self.lastRecv > self.heartbeat+(self.heartbeat//2):
            return self.disconnect()
        if (now - self.lastPing > self.heartbeat//10 and
            (now - self.lastSend > self.heartbeat or
             now - self.lastRecv > self.heartbeat)):
            self._send(MSG_PING)
            self.lastPing = now
        
        if data != None and len(data):
            self.bin += data

        while True:
            if len(self.bin) < 5:
                break

            cmd, i, dlen = struct.unpack("!BHH", self.bin[:5])
            if i == 0: return self.disconnect()
                      
            self.lastRecv = now
            if cmd == MSG_RSP:
                self.bin = self.bin[5:]

                self.log('>', cmd, i, '|', dlen)
                if self.state == CONNECTING and i == 1:
                    if dlen == STA_SUCCESS:
                        self.state = CONNECTED
                        dt = now - self.lastSend
                        info = ['ver', __version__, 'h-beat', self.heartbeat//1000, 'buff-in', self.buffin, 'dev', sys.platform+'-py']
                        if self.tmpl_id:
                            info.extend(['tmpl', self.tmpl_id])
                            info.extend(['fw-type', self.tmpl_id])
                        if self.fw_ver:
                            info.extend(['fw', self.fw_ver])
                        self._send(MSG_INTERNAL, *info)
                        try:
                            self.emit('connected', ping=dt)
                        except TypeError:
                            self.emit('connected')
                    else:
                        if dlen == STA_INVALID_TOKEN:
                            self.emit("invalid_auth")
                            print("Invalid auth token")
                        return self.disconnect()
            else:
                if dlen >= self.buffin:
                    print("Cmd too big: ", dlen)
                    return self.disconnect()

                if len(self.bin) < 5+dlen:
                    break

                data = self.bin[5:5+dlen]
                self.bin = self.bin[5+dlen:]

                args = list(map(lambda x: x.decode('utf8'), data.split(b'\0')))

                self.log('>', cmd, i, '|', ','.join(args))
                if cmd == MSG_PING:
                    self._send(MSG_RSP, STA_SUCCESS, id=i)
                elif cmd == MSG_HW or cmd == MSG_BRIDGE:
                    if args[0] == 'vw':
                        self.emit("V"+args[1], args[2:])
                        self.emit("V*", args[1], args[2:])
                elif cmd == MSG_INTERNAL:
                    self.emit("internal:"+args[0], args[1:])
                elif cmd == MSG_REDIRECT:
                    self.emit("redirect", args[0], int(args[1]))
                else:
                    print("Unexpected command: ", cmd)
                    return self.disconnect()

import socket

class Blynk(BlynkProtocol):
    def __init__(self, auth, **kwargs):
        self.insecure = kwargs.pop('insecure', False)
        self.server = kwargs.pop('server', 'blynk.cloud')
        self.port = kwargs.pop('port', 80 if self.insecure else 443)
        BlynkProtocol.__init__(self, auth, **kwargs)
        self.on('redirect', self.redirect)

    def redirect(self, server, port):
        self.server = server
        self.port = port
        self.disconnect()
        self.connect()

    def connect(self):
        print('Connecting to %s:%d...' % (self.server, self.port))
        s = socket.socket()
        s.connect(socket.getaddrinfo(self.server, self.port)[0][-1])
        try:
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        except:
            pass
        if self.insecure:
            self.conn = s
        else:
            try:
                import ussl
                ssl_context = ussl
            except ImportError:
                import ssl
                ssl_context = ssl.create_default_context()
            self.conn = ssl_context.wrap_socket(s, server_hostname=self.server)
        try:
            self.conn.settimeout(SOCK_TIMEOUT)
        except:
            s.settimeout(SOCK_TIMEOUT)
        BlynkProtocol.connect(self)

    def _write(self, data):
        #print('<', data)
        self.conn.write(data)
        # TODO: handle disconnect

    def run(self):
        data = b''
        try:
            data = self.conn.read(self.buffin)
            #print('>', data)
        except KeyboardInterrupt:
            raise
        except socket.timeout:
            # No data received, call process to send ping messages when needed
            pass
        except: # TODO: handle disconnect
            return
        self.process(data)

</pre>

### `Now let's check blynk is this work fine?`

# `Code: 1`

# `check_blynk.py`
<pre>
import BlynkLib
import network

BLYNK_AUTH = 'yqD8Pga0PduvJHOvahcRI3wH-Cj-cKju'


wifi = network.WLAN(network.STA_IF)
wifi.active(True)


while not wifi.isconnected():
    pass

print('IP:', wifi.ifconfig()[0])

blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.on("connected")
def blynk_connected(ping):
    print("Connecting.............")
    print('Blynk ready. Ping:', ping, 'ms')
    print("Connected!")

while True:
    blynk.run()
    
</pre>

# `Code: 2`
# `led1_blynk.py`

<pre>
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
</pre>

# `Code: 3`
# `led2_blynk.py`
<pre>
import BlynkLib
import network
import time
from machine import Pin

led1=Pin(14,Pin.OUT)
led2=Pin(13,Pin.OUT)
 
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
 
while True:
    blynk.run()
</pre>

# `Code: 4`
# `led2_blynk.py`
<pre>
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
</pre>

# `Code: 5`
# `dht_blynk.py`
<pre>
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

BLYNK_AUTH = 'yqD8Pga0PduvJHOvahcRI3wH-Cj-cKju'


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
</pre>

# `Save this with hcsr04.py`
<pre>
import machine, time
from machine import Pin

class HCSR04:
    """
    Driver to use the untrasonic sensor HC-SR04.
    The sensor range is between 2cm and 4m.
    The timeouts received listening to echo pin are converted to OSError('Out of range')
    """
    # echo_timeout_us is based in chip range limit (400cm)
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
        """
        trigger_pin: Output pin to send pulses
        echo_pin: Readonly pin to measure the distance. The pin should be protected with 1k resistor
        echo_timeout_us: Timeout in microseconds to listen to echo pin. 
        By default is based in sensor limit range (4m)
        """
        self.echo_timeout_us = echo_timeout_us
        # Init trigger pin (out)
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.trigger.value(0)

        # Init echo pin (in)
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)

    def _send_pulse_and_wait(self):
        """
        Send the pulse to trigger and listen on echo pin.
        We use the method `machine.time_pulse_us()` to get the microseconds until the echo is received.
        """
        self.trigger.value(0) # Stabilize the sensor
        time.sleep_us(5)
        self.trigger.value(1)
        # Send a 10us pulse.
        time.sleep_us(10)
        self.trigger.value(0)
        try:
            pulse_time = machine.time_pulse_us(self.echo, 1, self.echo_timeout_us)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110: # 110 = ETIMEDOUT
                raise OSError('Out of range')
            raise ex

    def distance_mm(self):
        """
        Get the distance in milimeters without floating point operations.
        """
        pulse_time = self._send_pulse_and_wait()

        # To calculate the distance we get the pulse_time and divide it by 2 
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.34320 mm/us that is 1mm each 2.91us
        # pulse_time // 2 // 2.91 -> pulse_time // 5.82 -> pulse_time * 100 // 582 
        mm = pulse_time * 100 // 582
        return mm

    def distance_cm(self):
        """
        Get the distance in centimeters with floating point operations.
        It returns a float
        """
        pulse_time = self._send_pulse_and_wait()

        # To calculate the distance we get the pulse_time and divide it by 2 
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.034320 cm/us that is 1cm each 29.1us
        cms = (pulse_time / 2) / 29.1
        return cms
</pre>

# `Code: 6`
# `distance_blynk.py`

<pre>
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

BLYNK_AUTH = 'yqD8Pga0PduvJHOvahcRI3wH-Cj-cKju'


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
</pre>
