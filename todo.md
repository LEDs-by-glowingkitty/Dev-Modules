
# Issues
- microphone doesn't seem to work with WLED, gives out nonesense data
  - -> check WLED docs for recommended mics
  - -> ask in WLED discord if they think there is a way to fix this in software?
- connecting via Matter to ESP32 H2 doesn't work on outside home wifi
  - -> test again at home

# Test
- ESP32 H2: write firmware with matter and SPI communication
- ESP32 H2: output SPI signal to ESP32 WROOM running WLED

# Questions
- how would a redesigned GlowTower PCB look like?
  - power circuit?
  - microphone?
  - esp32 WROOM + esp32 H2 Mini?
- what does currently not work?
