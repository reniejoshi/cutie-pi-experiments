from time import sleep
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)

try:
    lcd.clear()
    lcd.write_string('Hello, Cutie Pi!')
    sleep(5)
    lcd.clear()

except KeyboardInterrupt:
    lcd.clear()
