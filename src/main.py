import sys
import threading
from transcription import Transcriber
from translation import Translator
from display import OLEDDisplay
from button import ButtonHandler, PowerButtonHandler


vosk_to_libre_lang_codes = {
    "en" : "en",
    "cn" : "zh", 
    "ru" : "ru", 
    "fr" : "fr", 
    "de" : "de", 
    "es" : "es", 
    "pt" : "pt", 
    "gr" : "el", 
    "tr" : "tr", 
    "vn" : "vi", 
    "it" : "it", 
    "nl" : "nl",
    "ar" : "ar",
    "ca" : "ca",
    "fa" : "fa",
    "ph" : "tl",
    "uk" : "uk",
    "sv" : "sv",
    "jp" : "ja",
    "eo" : "eo",
    "hi" : "hi",
    "cs" : "cs",
    "po" : "pl",
    "ko" : "ko"
}

def vosk_code_to_libre(lang_code):
    if lang_code in vosk_to_libre_lang_codes.keys():
        return vosk_to_libre_lang_codes.get(lang_code)
    else
        print("Incorrect from language code")
        exit()

def transcribe(language, display):
    transcriber = Transcriber(language=language, display=display)
    transcriber.run()
    return

def translate(from_code, to_code, display):
    transcriber = Transcriber(language=from_code, display=display)
    translatator = Translator(from_code=from_code, to_code=to_code)
    transcriber.runWithTranslation(translatator,5)
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
    display = OLEDDisplay(font_size=10)

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
        translate(from_code=from_code, to_code=to_code, display=display)
        sys.exit()
    reboot.join()
    power.join()

main()