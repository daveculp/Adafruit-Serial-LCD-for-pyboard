# Adafruit-Serial-LCD-for-pyboard

This is a simple library for interfacing an Adfruit serial LCD to a pyboard.

To use, simply import the AfSerLCD module and create and AfSerLCD object.
The parameters are the UART number on the pyboatrd and the baud rate:

from AfSerLCD import *
lcd = AfSerLCD(6,9600)

You can then reference the object and use the AfSerLCD methods.  For example:

	print ("Configuring the LCD")
	print("\n===================================")
	brightness = int (input ("Enter brightness of LCD (0-255): "))
	contrast = int (input ("Enter contrast of LCD (0-255): "))
	r = int (input ("Enter red value of backlight (0-255): "))
	g = int (input ("Enter green value of backlight (0-255): "))
	b = int (input ("Enter blue value of backlight (0-255): "))
	line1 = input ("Enter first line of display:")
	line2 = input ("Enter second line of display:")
	print("\n===================================")

	lcd.setContrast(contrast)
	lcd.setBrightness(brightness)
	lcd.setBacklightColor(r,g,b)
	lcd.clearScreen()
	lcd.home()
	lcd.writeString(line1)
	lcd.setCursorPosition(2,1)
	lcd.writeString(line2) 
	print("Setting GPO's on LCD to LOW, check with a meter!")
	for x in range(1,5):
		lcd.setGPOState(x, False)


