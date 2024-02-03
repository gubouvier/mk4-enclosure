#!/usr/bin/python3 

import time
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
import syslog

MAX_TEMP = 25

while True:
    h, t = Adafruit_DHT.read_retry(11, 4)

    syslog.syslog(f"Humidity {h}% -- Temperature {t}C")

    if t > MAX_TEMP:
        syslog.syslog("Max temp reached, starting fan")
        start_fan()

    time.sleep(1)

def start_fan():
    pass