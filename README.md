# Micrologger

Simple logger based on esp32 with micropython.
It saves sgp30 sensor readings like amount of volatile organic compounds in ppm unit, 
carbon dioxide equivalent - CO2eq in bbp (parts per billion) and GPS coordinates.
Carbon dioxide equivalent (CO2eq) stands for a unit based on the global warming potential (GWP) of different greenhouse gases. 
The CO2eq unit measures the environmental impact of one tonne of these greenhouse gases in comparison to the impact of one tonne of CO2.


## Features

- Rapidly blinking led after uart initialization
- Slowly blinking led in time of waiting for gps fix
- Converting NMEA format data to decimal
- Save output into txt file
- If no gps there will not be output data 

## Tech

Detailed info:

- [Micropython] - esp32-20210623-v1.16
- [SGP30 library] - sgp30 micropython library 

# Connections

##### GPS:

* Vcc - esp 3v3 pin
* Gnd - Gnd
* Gps TX - RX1 pin
* Gps RX - TX1 pin
##### Sgp30:
* Vcc - esp 3v3 pin
* Gnd - Gnd
* SCL - D21 pin
* SDA - D22 pin

** If using raspberry pi pico use GP6 and GP7 pins.**

## Installation

Just copy and paste script into device flash memory.
Recommend to use [Thonny IDE] newest version.


## License

MIT


   [Micropython]: <https://micropython.org/download/esp32/>
   [SGP30 library]: <https://github.com/alexmrqt/micropython-sgp30>
   [Thonny IDE]: <https://thonny.org/>
