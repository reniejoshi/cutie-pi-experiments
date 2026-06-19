from gpiozero import RGBLED
from time import sleep
from signal import pause

led = RGBLED(red=14, green=15, blue=18)

print("Red: ", end="")
led.red = float(input())
print("Green: ", end="")
led.green = float(input())
print("Blue: ", end="")
led.blue = float(input())

sleep(1)

led.pulse()
pause()
