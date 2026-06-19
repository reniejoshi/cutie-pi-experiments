from gpiozero import LEDCharDisplay
from time import sleep
import random

display = LEDCharDisplay(18, 27, 4, 3, 2, 15, 14, dp=17)

display.value = str(random.randint(1, 9))

sleep(2)
