from enum import Enum
import RPi.GPIO as GPIO #
import time as time
class ButtonListener():
    LEFT = 1
    SELECT = 2
    RIGHT = 3
    def __init__(self):
        self.__runflag = True
    
    @staticmethod
    def __select_left(self,option):
        option[0] = ButtonListener.LEFT
        self.__runflag = False
        return

    @staticmethod
    def __select_select(self,option):
        option[0] = ButtonListener.SELECT
        self.__runflag = False
        return

    @staticmethod
    def __select_right(self,option):
        option[0] = ButtonListener.RIGHT
        self.__runflag = False
        return

    def selectOption(self,selectedOption):
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BCM) # Use BCM pin numbering
        GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 5 to be an input pin and set initial value to be pulled low (off
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 6 to be an input pin and set initial value to be pulled low (off)
        GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 13 to be an input pin and set initial value to be pulled low (off)
        GPIO.add_event_detect(5,GPIO.RISING,callback=lambda x: ButtonListener.__select_left(self,selectedOption)) # Setup event on pin 12 rising edge
        GPIO.add_event_detect(17,GPIO.RISING,callback=lambda x: ButtonListener.__select_select(self,selectedOption)) # Setup event on pin 12 rising edge
        GPIO.add_event_detect(13,GPIO.RISING,callback=lambda x: ButtonListener.__select_right(self,selectedOption)) # Setup event on pin 12 rising edge
        
        
        while self.__runflag:
            pass
        self.__runflag = True
        GPIO.cleanup()
        time.sleep(0.01) #Fixes issues with GPIO segmenation faults 
        return
