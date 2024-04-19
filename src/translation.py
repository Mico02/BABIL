import subprocess
from libretranslatepy import LibreTranslateAPI
from display import OLEDDisplay
import time

class Translator():
    def __init__(self, from_code, to_code):

        #Setting instance variables for from and to codes
        self.__from_code = from_code
        self.__to_code = to_code
        
        #Starting local translation API 
        self.__process = subprocess.Popen(["libretranslate"])
        time.sleep(8)
        #Initializing translator API
        self.__translator = LibreTranslateAPI("http://127.0.0.1:5000")

        #initialize display
        self.__display = OLEDDisplay(font_size = 10)


    def run(self, words, threadFlag):
        
        phrase = ' '.join(words)
        if len(phrase) > 0:
            translated = self.__translator.translate(q=phrase,source=sekf.__from_code, target=self.__to_code)
            self.__display.displayWords(translated.split(" "))
            print(translated)
        threadFlag[0] = False
        exit()

    def runTest(self, phrase):
        f = open("translation_test.txt","a")
        translated = self.__translator.translate(q=phrase,source=self.__from_code, target=self.__to_code)
        f.write(translated + " ")
        f.close()

    def __del__(self):
        self.__process.terminate()
