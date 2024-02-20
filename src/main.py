import sys
import threading
from transcription import Transcriber
from display import OLEDDisplay
from button import ButtonHandler, PowerButtonHandler

def transcribe(language, display):
    transcriber = Transcriber(language=language, display=display)
    transcriber.run()
    return

def translate(from_code, to_code):
    return

def main():

    #initializing buttonhandler and power/reboot thread
    button = ButtonHandler()
    powerbutton = PowerButtonHandler()
    reboot = threading.Thread(target=button.reboot_reselect)
    power = threading.Thread(target=powerbutton.wait_for_press)
    reboot.start()
    power.start()
    #Initializing display object
    display = OLEDDisplay(font_size=15)

    #Read cmd arguements 
    mode = sys.argv[1]
    if mode == '-c':
        language = sys.argv[2]
        transcribe(language,display)
        sys.exit()
    else: 
        from_code = sys.argv[1]
        to_code = sys.argv[2]
        if from_code == to_code:
            transcribe(language=from_code)
            sys.exit()
        translate(from_code=from_code, to_code=to_code)
        sys.exit()
    reboot.join()
    power.join()

main()