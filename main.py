from machine import Pin
from time import sleep
import time
import ntptime
import door

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('1776 2.4G', 'babycat2')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

led = Pin(2, Pin.OUT)
thedoor =  door()
thedoor.dooropen()

do_connect()
print("Local time before synchronization：%s" %str(time.localtime()))
ntptime.settime()
print("Local time after synchronization：%s" %str(time.localtime()))

while True:
  led.value(not led.value())
  sleep(0.5)