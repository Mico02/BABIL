import sys
import os
import time
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib'))

#Importing libraries for outputting to the display
from waveshare_OLED import config
from waveshare_OLED import OLED_1in51
from PIL import Image,ImageDraw,ImageFont

#Setting the device to work using SPI
config.Device_SPI = 1
config.Device_I2C = 0


display = None #Global object that serves as the object for display


def initDisplay(font_size = 14):
    ''' 
    Intializes the diplay and other parameters for display to function
    
    Args:
        font_size  (int): font size 
    '''
    display = OLED_1in51.OLED_1in51()
    display.Init()
    display.clear()
    image = 

def displayWord(word):

