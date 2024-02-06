import RPi.GPIO as GPIO # ImportRaspberry Pi GPIO library
import subprocess
import time
def callback_reboot(exit_flag):
    print("Reboot")
    exit_flag[0] = True
    time.sleep(1)
    result = subprocess.Popen(["python3" ,"src/main.py","-c","en"])
    exit()
def callback_shutdown(exit_flag):
    print("Shutdown")
    exit_flag[0] = True
    time.sleep(1)
    exit()
def start_listener(exit_flag):
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BCM) # Use physical pin numbering
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

    GPIO.add_event_detect(5,GPIO.RISING,callback=lambda x: callback_reboot(exit_flag)) # Setup event on pin 12 rising edge
    GPIO.add_event_detect(6,GPIO.RISING,callback=lambda x: callback_shutdown(exit_flag)) # Setup event on pin 12 rising edge
    GPIO.add_event_detect(13,GPIO.RISING,callback=lambda x: callback_shutdown(exit_flag)) # Setup event on pin 12 rising edge
    try:
        while True:
            pass  # Keep the thread alive
    finally:
        GPIO.cleanup()
        exit()