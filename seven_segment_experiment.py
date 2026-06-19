from gpiozero import LEDCharDisplay
from time import sleep

display = LEDCharDisplay(3, 5, 7, 8, 10, 11, 12, 16)

for char in '0123456789':
    display.value = char
    sleep(1)