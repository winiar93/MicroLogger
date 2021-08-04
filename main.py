import time
import math
import machine
from machine import UART,Pin, I2C
import adafruit_sgp30
import machine

led = Pin(2, Pin.OUT)
uart = UART(2, 9600)

for i in range(50):
    led.on()
    time.sleep(0.05)
    led.off()
    time.sleep(0.05)
    
try:
  i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
  devices = i2c.scan()
  if len(devices) == 0:
    print("Error: no I2C device !")
  else:
    for d in devices:
      print("Decimal address: ",d," | Hexa address: ",hex(d))
except Exception as e:
  print("Exception: {}".format(e))
  
    
try:
  co2_eq = 400
  tvoc = 0
  sgp30 = adafruit_sgp30.Adafruit_SGP30(
    i2c,
    address=0x58)
  print("SGP30 serial #", [hex(i) for i in sgp30.serial])
  sgp30.iaq_init()
  print("Waiting 5 seconds for SGP30 initialization.")
  time.sleep(1)
except Exception as e:
  print("Exception: {}".format(e))

while True:
    while uart.any():
        raw_data =  str(uart.read())
        if "GNRMC" in raw_data:
            try:
                position_gps = raw_data.split("GNRMC",1)[1]
                lat = position_gps.split(",")[3]
                lat_dir = position_gps.split(",")[4]
                lat = round(math.floor(float(lat) / 100) + (float(lat) % 100) / 60, 6)
                lon = position_gps.split(",")[5:6][0]
                lon = round(math.floor(float(lon) / 100) + (float(lon) % 100) / 60, 6)
                lon_dir = position_gps.split(",")[6]

                co2_eq, tvoc = sgp30.iaq_measure()
                print(lat,lat_dir, lon, lon_dir, 'co2eq = ' + str(co2_eq) + ' ppm \t tvoc = ' + str(tvoc) + ' ppb')
                f = open('data.txt', 'a')
                f.write("{} {},{} {} ,{},{}".format(lat,lat_dir, lon, lon_dir,co2_eq,tvoc)+"\n")
                f.close()
                time.sleep(1)
            except Exception as e:
                print(e)
                led.on()
                time.sleep(0.5)
                led.off()