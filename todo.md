
# Issues
- microphone doesn't seem to work with WLED, gives out nonesense data
  - -> check WLED docs for recommended mics
  - -> ask in WLED discord if they think there is a way to fix this in software?
- connecting via Matter to ESP32 H2 doesn't work on outside home wifi
  - -> test again at home

# Test Home
- ESP32 H2: test matter connection
- ESP32 WROOM: test matter connection

# Test xHain
- WS2812B LEDs: how much current do 240 really consume at max power? at 5V? 4.8V? 4.1V?
- ESP32 WROOM vs ESP32 H2 MINI: how much power does each consume using matter?
- EPS32 WROOM: if EN pin is low, does it really not consume any power?

# Other tests
- ESP32 H2: write firmware with matter and SPI communication
- ESP32 H2: output SPI signal to ESP32 WROOM running WLED

# PCB design tasks
- TPS54202 Buck converter PCB
  - -> for VBUS to 3.3V for ESP32 WROOM and ESP32 H2
- Buck converter PCB for large output
  - -> for LEDs
- order not populated pcbs, order components from LCSC and assemble manually?

# Questions
- how would a redesigned GlowTower PCB look like?
  - power circuit?
  - microphone?
  - esp32 WROOM + esp32 H2 Mini?
  - does another esp32 wroom instead of H2 mini makes more sense? (better availability)
- what does currently not work?



# - build circuit with 5V buck converter where it requests 4.1V, using potty
# -> use TPS54202 and connect it to VBUS, thats the best solution for consistant 3.3V power for ESP32.