import pyb

#define our commands
LCD_COMMAND             =   0xFE
DISPLAY_ON              =   0x42 
DISPLAY_OFF             =   0x46
SET_BRIGHTNESS          =   0x99
SET_SAVE_BRIGHTNESS     =   0x98
SET_CONTRAST            =   0x50
SET_SAVE_CONTRAST       =   0x91
AUTOSCROLL_ON           =   0x51
AUTOSCROLL_OFF          =   0x52
CLEAR_DISPLAY           =   0x58
SET_SPLASH_SCREEN       =   0x40
SET_CURSOR_POS          =   0x47
GO_HOME                 =   0x48
CURSOR_BACK             =   0x4C
CURSOR_FORWARD          =   0x4D
UNDERLINE_CURSOR_ON     =   0x4A
UNDERLINE_CURSOR_OFF    =   0x54
BLOCK_CURSOR_ON         =   0x53
BLOCK_CURSOR_OFF        =   0x54
SET_BACKLIGHT_COLOR     =   0xD0
SET_LCD_SIZE            =   0xD1
CREATE_CUSTOM_CHAR      =   0x4E
SAVE_CUSTOM_CHAR        =   0XC1
LOAD_CUSTOM_CHAR        =   0XC0
SET_GPO_OFF             =   0x56
SET_GPO_ON              =   0X57

class AfSerLCD:
    def __init__(self, uartNum, baud=9600):
        self.uart = pyb.UART( uartNum, baud) 
    
    def sendCommand(self, command):
        self.uart.writechar(LCD_COMMAND)
        self.uart.writechar(command)
    
    def writeString(self,string):
        self.uart.write(string)
        
    def clearScreen(self):
        self.sendCommand(CLEAR_DISPLAY)
        
    def setContrast(self,contrast, save=False):
        if save == False:
            self.sendCommand(SET_CONTRAST)
        else:
            self.sendCommand(SET_SAVE_CONTRAST)
        self.uart.writechar(contrast)
    
    def setBrightness(self,brightness, save=False):
        if save == False:
            self.sendCommand(SET_BRIGHTNESS)
        else:
            self.sendCommand(SET_SAVE_BRIGHTNESS)
        self.uart.writechar(brightness)
        
    def setSaveBrigthness(self, brightness):
        self.sendCommand(SET_SAVE_BRIGHTNESS)
        self.uart.writechar(brightness)
        
    def displayOn(self):
        self.sendCommand(DISPLAY_ON)
    
    def displayOff(self):
        self.sendCommand(DISPLAY_OFF)
        
    def home(self):
        self.sendCommand(GO_HOME)
    
    def setCursorPosition(self, row,col):
        self.sendCommand(SET_CURSOR_POS)
        self.uart.writechar(col)
        self.uart.writechar(row)
    
    def setBacklightColor(self,r,g,b):
        self.sendCommand(SET_BACKLIGHT_COLOR)
        self.uart.writechar(r)
        self.uart.writechar(g)
        self.uart.writechar(b)
    
    def setAutoscroll(self, scrollState):
        if scrollState == True:
            self.sendCommand(AUTOSCROLL_ON)
        else:
            self.sendCommand(AUTOSCROLL_OFF)
            
    def setSplashScreen(self, splashMsg):
        self.sendCommand(SET_SPLASH_SCREEN)
        self.uart.write(splashMsg)
    
    def cursorBack(self):
        self.sendCommand(CURSOR_BACK )
        
    def cursorForward(self):
        self.sendCommand(CURSOR_FORWARD)
        
    def setUnderlineCursor(state=True):
        if state == True:
            self.sendCommand(UNDERLINE_CURSOR_ON)
        else:
            self.sendCommand(UNDERLINE_CURSOR_OFF)
    
    def setBlockCursor(state=True):
        if state == True:
            self.sendCommand(BLOCK_CURSOR_ON)
        else:
            self.sendCommand(BLOCK_CURSOR_OFF)
    
    def setLCDSize(self, rows=2, cols=16):
        self.sendCommand(SET_LCD_SIZE)
        self.uart.writechar(rows)
        self.uart.writechar(cols)
        
    def setGPOState(self, gpoNum, state=False):
        if gpoNum < 1 or gpoNum > 4:
            print("ERROR: gpoNum must be 1-4 in setGPOState")
            return
        if state == False:
            self.sendCommand(SET_GPO_OFF)
            self.uart.writechar(gpoNum)
            return
        elif state == True:
            self.sendCommand(SET_GPO_ON)
            self.uart.writechar(gpoNum)
            return 
        else:
            print("ERROR: Unknown state for setGPOState.")
            
    def createCustomChar(self, charNum, byteList):
        if charNum < 0 or chatNum > 7:
            print("ERROR: charnum must be 0-7 in createCustomChar.")
            return
        if len(byteList) > 8:
            print("ERROR: byteList must be list of 8 buyes in createCustomChar.")
            return
        self.sendCommand(CREATE_CUSTOM_CHAR)
        for char in byteList:
            self.uart.writechar(char)
            
    
    
    
    
            
    
            
