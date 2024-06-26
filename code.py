# Get signal from a button
# One pole to 3.3V and one to a GPIO pin

import board
import time
import digitalio
import board
import neopixel
from ledPixelsPico import *

# Chnage number of LEDs here
nPix = 18

# Defines state of LEDs 
def turnon():
    for i in range (nPix):
        pixels[i] = (220, 220, 190)
        
def turnoff():
    for i in range (nPix):
        pixels[i] = (0, 0, 0)

# Change GPIO for LEDs
pixels = neopixel.NeoPixel(board.GP13, nPix)

# Change GPIO for button here
timerBtn = digitalio.DigitalInOut(board.GP28)
timerBtn.pull = digitalio.Pull.DOWN

mode="off"

#Controls how switch behaves
while True:
    if timerBtn.value:
        while timerBtn.value:
            time.sleep(0.1)
        if mode == "off":
            mode="on"
            turnon()
        else:
            mode="off"
            turnoff()
        print("mode:", mode)

    
        
