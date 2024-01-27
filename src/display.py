import sys
import os
import time
import queue
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib'))

#Importing libraries for outputting to the display
from waveshare_OLED import config
from waveshare_OLED import OLED_1in51
from PIL import Image,ImageDraw,ImageFont

class OLEDDisplay:
    __display = None #object for display
    __image = None #object for image on the display
    __draw = None #object for drawing on the image
    __font = None #object that stores the text font
    def __init__(self, font_size = 14):
        ''' 
        Intializes the diplay and other parameters for display to function, font size is 14 by default
        
        Args:
            font_size  (int): font size 
        '''

        #Setting the device to work using SPI
        config.Device_SPI = 1
        config.Device_I2C = 0

        #Intializes the diplay, image, drawing object, and font
        self.__display = OLED_1in51.OLED_1in51()
        self.__display.Init()
        self.__display.clear()
        self.__font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), font_size)

    def displayWord(self, word):
        '''
        Displays the give word onto the OLED display

        Args:
            word (str): the word to be displayed
        '''
        self.__image = Image.new('1',(self.__display.width, self.__display.height), "WHITE")
        self.__draw = ImageDraw.Draw(self.__image)
        self.__draw.text((40,20), word, font=self.__font, fill=0)
        self.__image = self.__image.rotate(self.__rotation)
        self.__display.ShowImage(self.__display.getbuffer(self.__image))

    def displayWords(self, words):
        for word in words:
            self.displayWord(word)
            time.sleep(0.1)


    def clear(self, display):
        self.__display.clear()

    def changeFontSize(self, font_size):
        ''' 
        Changes the current font size of the display text
    
        Args:
            font_size  (int): font size 
        '''
        self.__font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), font_size)


    '''
    BROKEN
    def rotate(self, degrees):
        THIS METHOD REQURES THAT THERE BE TEXT ALREADY ON DISPLY ON THE SCREEN, OTHERWISE THERE IS NO 
        IMAGE TO ROTATE !!
        self.__image = self.__image.rotate(degrees)
        self.__display.ShowImage(self.__display.getbuffer(self.__image))
    '''


    
