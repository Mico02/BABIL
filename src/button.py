from enum import Enum
class ButtonListener(self, Enum):
    LEFT = 1
    SELECT = 2
    RIGHT = 3
    def __init__(self):
        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BCM) # Use BCM pin numbering
        GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 5 to be an input pin and set initial value to be pulled low (off)
        GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 6 to be an input pin and set initial value to be pulled low (off)
        GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 13 to be an input pin and set initial value to be pulled low (off)
        return

    def __select_left(option,flag):
        option[0] = ButtonListener.LEFT
        flag = True
        return
    def __select_select(option,flag):
        option[0] = ButtonListener.SELECT
        flag = True
        return
    def __select_select(option,flag):
        option[0] = ButtonListener.RIGHT
        flag = True
        return

    def selectOption(selectedOption):
        GPIO.add_event_detect(5,GPIO.RISING,callback=lambda x: __select_left(selectedOption,flag)) # Setup event on pin 12 rising edge
        GPIO.add_event_detect(6,GPIO.RISING,callback=lambda x: __select_select(selectedOption,flag)) # Setup event on pin 12 rising edge
        GPIO.add_event_detect(13,GPIO.RISING,callback=lambda x: __select_right(selectedOption,flag)) # Setup event on pin 12 rising edge
        while not flag:
            pass
        GPIO.cleanup()
        exit()
