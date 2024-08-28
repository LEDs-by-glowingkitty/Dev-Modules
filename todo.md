
# What modules does GlowTower / GlowLight need?
- 1x USB PD USB-C port
- 1x USB PD IC (requests 9V to 20V)
- 1x Buck converter 5V (-> design pcb module)
- 1x Buck converter 3.3V (-> design pcb module)
- 2x ESP32 WROOM (or 1x ESP32 WROOM and 1x ESP32 H2 or C6)
- 1x microphone (-> find new mic?)
- 2x levelshifter
- 4x big cap

# What modules does GlowTower / GlowLight not need anymore?
- 4x MOSFET power switch for LEDs (because 5V buck converter will now only power LEDs and therefore LEDs can be easily disconnected from power by turning on/off converter)
- 1x ideal diode (same reason)
- 1x CP2101N (because programmming is done via external ESP32 programmer once and then via wifi)
- 1x 3.3V LDO (will be replaced with 3.3V buck converter)

# Next steps
1. design missing pcb modules
2. order missing pcb modules
3. test updated pcb design with pcb modules
4. once testing completed, design updated completed pcb
5. order updated completed GlowTower PCB


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