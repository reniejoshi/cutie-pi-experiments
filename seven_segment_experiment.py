from gpiozero import LEDCharDisplay
from time import sleep

display = LEDCharDisplay(2, 3, 4, 17, 14, 15, 16, 18, 27, dp=11)

for char in '0123456789':
    display.value = char
    sleep(1)