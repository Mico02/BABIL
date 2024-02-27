import RPi.GPIO as GPIO
import time
import os 
import sys
import signal
import subprocess
class ButtonHandler:
    """This provides a Python class to control Button GPIO with different functions"""
    #Defining a const value that represents the buttons for left, right, select
    LEFT = 1   
    RIGHT = 2  
    SELECT = 3 

    _BCM_PINS = [5, 6, 13]   #BCM GPIO pin connections for the buttons
    _PHY_PINS = [29, 31, 33] #Physical GPIO pin connections for the buttons
    def __init__(self, power_button=True):
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
    def __select_left(self,selectedOption):
        selectedOption[0] = ButtonHandler.LEFT
        self.__runFlag = False
        
    def __select_right(self,selectedOption):
        selectedOption[0] = ButtonHandler.RIGHT
        self.__runFlag = False
        
    def __select_select(self,selectedOption):
        selectedOption[0] = ButtonHandler.SELECT
        self.__runFlag = False

    def __reboot(self):
        subprocess.Popen(["python3" ,"src/select_language.py"])
        print("GOODBYE BABIL")
        os.kill(os.getpid(),signal.SIGKILL)

    def selectOption(self,selectedOption):
        self.__runFlag = True
        if self.__mode == GPIO.BCM:
            GPIO.add_event_detect(self._BCM_PINS[0], GPIO.RISING, callback=lambda x: ButtonHandler.__select_left(self,selectedOption)  ,bouncetime=250)
            GPIO.add_event_detect(self._BCM_PINS[1], GPIO.RISING, callback=lambda y: ButtonHandler.__select_right(self,selectedOption) ,bouncetime=250)
            GPIO.add_event_detect(self._BCM_PINS[2], GPIO.RISING, callback=lambda z: ButtonHandler.__select_select(self,selectedOption),bouncetime=250)
        elif self.__mode == GPIO.BOARD:
            GPIO.add_event_detect(self._PHYS_PINS[0], GPIO.RISING, callback=lambda x: ButtonHandler.__select_left(self,selectedOption)  ,bouncetime=250)
            GPIO.add_event_detect(self._PHYS_PINS[1], GPIO.RISING, callback=lambda y: ButtonHandler.__select_right(self,selectedOption) ,bouncetime=250)
            GPIO.add_event_detect(self._PHYS_PINS[2], GPIO.RISING, callback=lambda z: ButtonHandler.__select_select(self,selectedOption),bouncetime=250)
        else:
            print("Error: GPIO Mode not set", file=sys.err)
        while self.__runFlag:
            pass
        time.sleep(0.001) #prevents seg fault 
        GPIO.remove_event_detect(self._BCM_PINS[0])
        GPIO.remove_event_detect(self._BCM_PINS[1])
        GPIO.remove_event_detect(self._BCM_PINS[2])
        return

    def reboot_reselect(self):
        self.__runFlag = True
        if self.__mode == GPIO.BCM:
            GPIO.add_event_detect(self._BCM_PINS[0], GPIO.RISING, callback=lambda x: ButtonHandler.__reboot(self)  ,bouncetime=250)
            GPIO.add_event_detect(self._BCM_PINS[1], GPIO.RISING, callback=lambda y: ButtonHandler.__reboot(self) ,bouncetime=250)
            GPIO.add_event_detect(self._BCM_PINS[2], GPIO.RISING, callback=lambda x: ButtonHandler.__reboot(self)  ,bouncetime=250)
        elif self.__mode == GPIO.BOARD:
            GPIO.add_event_detect(self._PHYS_PINS[0], GPIO.RISING, callback=lambda x: ButtonHandler.__reboot(self) ,bouncetime=250)
            GPIO.add_event_detect(self._PHYS_PINS[1], GPIO.RISING, callback=lambda y: ButtonHandler.__reboot(self) ,bouncetime=250)
            GPIO.add_event_detect(self._PHYS_PINS[2], GPIO.RISING, callback=lambda y: ButtonHandler.__reboot(self) ,bouncetime=250)
        else:
            print("Error: GPIO Mode not set", file=sys.err)

    def __del__(self):
        GPIO.cleanup()

class PowerButtonHandler():
    def __init__(self, pButtonPinBCM=26, pButtonPinPhys=37):
        '''
        Initializes Power Button Handler 
        '''
        GPIO.setwarnings(False) #Disabling GPIO warnings

        #Setting the pin numbers for an instance class member
        self.__pButtonPinBCM=pButtonPinBCM
        self.__pButtonPinPhys=pButtonPinPhys

        #Getting the current GPIO mode so that there is no conflict with any other program using the GPIO
        self.__mode = GPIO.getmode() 

        if self.__mode == None: #if the GPIO layout is not set, set it to BCM
            GPIO.setmode(GPIO.BCM)
            self.__mode = GPIO.BCM
        elif self.__mode == GPIO.BOARD: #if the GPIO layout is set to physical, then setup using phys pin numbers
            GPIO.setup(self.__pButtonPinPhys, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #Program will reach here if the GPIO was/is set to BCM, GPIO pins are the set using BCM pin numbers
        GPIO.setup(self.__pButtonPinBCM,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    def __shutdown(self,channel):
        print("SHUTTING DOWN!")
        os.system("sudo shutdown -h now")
        sys.exit()

    def wait_for_press(self):
        self.__flag = True
        if self.__mode == GPIO.BCM:
           GPIO.add_event_detect(self.__pButtonPinBCM, GPIO.RISING, callback=self.__shutdown, bouncetime=500)
        elif self.__mode == GPIO.BOARD:
            GPIO.add_event_detect(self.__pButtonPinPhys, GPIO.RISING, callback=self.__shutdown, bouncetime=500)
        while self.__flag:
            pass
    def stop_waiting(self):
        self.__flag = False;


