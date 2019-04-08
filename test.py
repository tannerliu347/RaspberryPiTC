#!/usr/bin/python
# Raspi -- MAX31855
# 3.3v  -- Vin
# GND   -- GND
# 36    -- Do
# 38    -- CS
# 40    -- CLK
from max31855 import MAX31855, MAX31855Error
import time

cs_pin = 20
clock_pin = 21
data_pin = 16
units = "f"
thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units)
while True:
    print(thermocouple.get())
    time.sleep(1)
thermocouple.cleanup()