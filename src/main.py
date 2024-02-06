import sys
from transcription import Transcriber
from display import OLEDDisplay
from buttonlistener import start_listener
from buttonlistener import ButtonInterrupt
import threading

def transcribe(language, display):
    transcriber = Transcriber(language=language, display=display)
    transcriber.run()
    return

def translate(from_code, to_code):
    return

def main():
    #Initializing display object
    display = OLEDDisplay(font_size=15)

    #Read cmd arguements 
    mode = sys.argv[1]
    if mode == '-c':
        language = sys.argv[2]
        transcribe(language,display)
        exit()
    else: 
        from_code = sys.argv[1]
        to_code = sys.argv[2]
        if from_code == to_code:
            transcribe(language=from_code)
            exit()
        translate(from_code=from_code, to_code=to_code)
        exit()

#Starting button listener
run_flag = True
listener_thread = threading.Thread(target=start_listener)
listener_thread.start()

main()


listener_thread.join()