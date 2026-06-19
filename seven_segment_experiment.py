from gpiozero import LEDCharDisplay
from time import sleep

display = LEDCharDisplay(18, 27, 4, 3, 2, 15, 14, dp=17)

for char in 'HELL0ROD':
    display.value = char
    sleep(1)

display.value = " "
sleep(1)

while True:
    for char in '2046':
        display.value = char
        sleep(1)
