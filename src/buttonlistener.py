import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

class ButtonInterrupt(Exception):
    pass
def callback(channel):
    print("Interrupt")
    raise ButtonInterrupt
def start_listener():
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BCM) # Use physical pin numbering
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

    GPIO.add_event_detect(5,GPIO.RISING,callback=callback) # Setup event on pin 12 rising edge
    GPIO.add_event_detect(6,GPIO.RISING,callback=callback) # Setup event on pin 12 rising edge
    GPIO.add_event_detect(13,GPIO.RISING,callback=callback) # Setup event on pin 12 rising edge
    try:
        while True:
            pass  # Keep the thread alive
    finally:
        GPIO.cleanup()
        exit()