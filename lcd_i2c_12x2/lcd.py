import lcddriver
from time import *

lcd = lcddriver.lcd()

# lcd.lcd_clear();
lcd.lcd_display_string("*** nacitani ***", 1)
lcd.lcd_display_string("1234567890123456", 2)
