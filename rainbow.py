from gpiozero import RGBLED
from time import sleep
from signal import pause

led = RGBLED(red=14, green=15, blue=18)

led.red = 1.0
led.green = 0.5
led.blue = 0.0

sleep(2)

led.pulse()
pause()