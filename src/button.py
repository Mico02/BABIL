import RPi.GPIO as GPIO
class ButtonHandler:
    def __init__(self):
        BCM_PINS = [5, 6, 13]   #BCM GPIO pin connections for the buttons
        PHY_PINS = [29, 31, 33] #Physical GPIO pin connections for the buttons
        GPIO.setwarnings(False) #Disabling GPIO warnings
        
        #Getting the current GPIO mode so that there is no conflict with any other program using the GPIO
        self.__mode = GPIO.getmode() 

        if self.__mode == None: #if the GPIO layout is not set, set it to BCM
            GPIO.setmode(GPIO.BCM)
            self.__mode = GPIO.BCM
        elif self.__mode == GPIO.BOARD: #if the GPIO layout is set to physical, then setup using phys pin numbers
            for pin in PHY_PINS:
                GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                return
            
        #Program will reach here if the GPIO was/is set to BCM, GPIO pins are the set using BCM pin numbers
        for pin in BCM_PINS:
            GPIO.setup(pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def __del__(self):
        GPIO.clean()

