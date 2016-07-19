# Adafruit-Serial-LCD-for-pyboard

This is a simple library for interfacing an Adfruit serial LCD to a pyboard.
The LCD can be purchased [here] (https://www.adafruit.com/product/782):

To use, simply import the afserLCD module and create an AfSerLCD object.
The parameters are the UART number on the pyboard and the baud rate.  If a 
baud rate is not specified the object defaults to 9600 baud.

Example:

```python
from afserlcd import *
lcd = AfSerLCD(6,9600)
```

You can then reference the object and use the AfSerLCD methods.  For example:

```python
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
```
### API Reference:

*	writeString(string)
*	clearScreen()
*	setContrast(contrast, save=False)
*	setBrightness(brightness, save=False):
*	displayOn()
*	displayOff()
*	home()
*	setCursorPosition(row,col)
*	setBacklightColor(r,g,b)
*	setAutoscroll(scrollState)
*	setSplashScreen(splashMsg):
*	cursorBack():
*	cursorForward():
*	setUnderlineCursor(state=True)
*	setBlockCursor(state=True)
*	setLCDSize(rows=2, cols=16):
*	setGPOState(gpoNum, state=False):
*	createCustomChar(charNum, byteList):


