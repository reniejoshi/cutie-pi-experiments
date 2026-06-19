from gpiozero import LEDCharDisplay
from time import sleep

display = LEDCharDisplay(18, 27, 4, 3, 2, 15, 14, dp=17)

for char in '0123456789':
    display.value = char
    sleep(1)