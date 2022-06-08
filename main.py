from machine import UART, Pin, I2C
import time
import onewire
from time import sleep_us ,ticks_us, ticks_ms
from micropyGPS import MicropyGPS
import adafruit_sgp30


def main():
    uart = UART(1,baudrate=9600, bits=8, parity=None, stop=1, timeout=5000, rxbuf=1024)
    i2c= machine.I2C(1)
    gps = MicropyGPS()
    
    sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c,address=0x58)
    sgp30.iaq_init()
    time.sleep(2)
    
    while True:
    #for _ in range(10): for debugging
        buf = uart.readline()
        try:
            for char in buf:
                gps.update(chr(char))  # Note the conversion to to chr, UART outputs ints normally
   
            g_time = gps.timestamp
            g_alt = gps.altitude
            glat = gps.latitude_string()
            glon = gps.longitude_string()
            co2eq, tvoc = sgp30.iaq_measure()
            f = open('data.txt', 'a')
            f.write(f'{g_time};{g_alt};{glat};{glon};{co2eq};{tvoc}'+"\n")
            f.close()
        except Exception as e:
            print(e)
            pass
        
    
if __name__ == "__main__":
  print('...running main, GPS testing')
  main()