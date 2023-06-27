from machine import Pin
import time

led = Pin("LED", Pin.OUT)


def blink(num):
    for i in range(num*2):
        led.toggle()
        time.sleep(0.3)


while True:
    blink(3)
    time.sleep(100)

