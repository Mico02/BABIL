import subprocess
from transcription import Transcriber
from libretranslatepy import LibreTranslateAPI
from display import OLEDDisplay

class Translator(Transcriber):
    def __init__(self, from_code, to_code):

        #Setting instance variables for from and to codes
        self.__from_code = from_code
        self.__to_code = to_code
        
        #Starting local translation API 
        subprocess.run(["libretranslate"])

        #Initializing translator API
        self.__translator = LibreTranslateAPI("http://127.0.0.1:5000")

        #initialize display
        self.__display = OLEDDisplay(font_size = 15)


    def run(self, words):
        translated = self.__translator.translate(q=words,source=self.__from_code, target=self.__to_code)
        self.__display.displayWords(translated.split(" "))