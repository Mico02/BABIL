"""This provides a Python class to control Button GPIO with different functions"""

import RPi.GPIO as GPIO
import time
import faulthandler
faulthandler.enable()
class ButtonHandler:
    #Defining a const value that represents the buttons for left, right, select
    LEFT = 1   
    RIGHT = 2  
    SELECT = 3 

    _BCM_PINS = [5, 6, 13]   #BCM GPIO pin connections for the buttons
    _PHY_PINS = [29, 31, 33] #Physical GPIO pin connections for the buttons
    def __init__(self):
        '''
        Initializes Button Handler 
        '''
        GPIO.setwarnings(False) #Disabling GPIO warnings
        
        #Getting the current GPIO mode so that there is no conflict with any other program using the GPIO
        self.__mode = GPIO.getmode() 

        if self.__mode == None: #if the GPIO layout is not set, set it to BCM
            GPIO.setmode(GPIO.BCM)
            self.__mode = GPIO.BCM
        elif self.__mode == GPIO.BOARD: #if the GPIO layout is set to physical, then setup using phys pin numbers
            for pin in self._PHY_PINS:
                GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                return
            
        #Program will reach here if the GPIO was/is set to BCM, GPIO pins are the set using BCM pin numbers
        for pin in self._BCM_PINS:
            GPIO.setup(pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    def __select_left(self,selectedOption,flag):
        selectedOption[0] = ButtonHandler.LEFT
        self.__runFlag = False
        print("this is left")
    def __select_right(self,selectedOption,flag):
        selectedOption[0] = ButtonHandler.RIGHT
        self.__runFlag = False
        print("this is right")
    def __select_select(self,selectedOption,flag):
        selectedOption[0] = ButtonHandler.SELECT
        self.__runFlag = False
        print("this is select")

    def selectOption(self,selectedOption):
        self.__runFlag = True
        GPIO.add_event_detect(self._BCM_PINS[0], GPIO.RISING, callback=lambda x: self.__select_left(selectedOption,self.__runFlag))
        GPIO.add_event_detect(self._BCM_PINS[1], GPIO.RISING, callback=lambda x: self.__select_right(selectedOption,self.__runFlag))
        GPIO.add_event_detect(self._BCM_PINS[2], GPIO.RISING, callback=lambda x: self.__select_select(selectedOption,self.__runFlag))
        print("waiting")
        while self.__runFlag:
            pass
        time.sleep(0.001) #prevents seg fault 
        GPIO.remove_event_detect(self._BCM_PINS[0])
        GPIO.remove_event_detect(self._BCM_PINS[1])
        GPIO.remove_event_detect(self._BCM_PINS[2])
        return


    def __del__(self):
        GPIO.cleanup()

