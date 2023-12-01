import sounddevice
import sys
import queue
import json
import time
from libretranslatepy import LibreTranslateAPI
from vosk import Model, KaldiRecognizer
from display import OLEDDisplay


#setting up call back for continous audio capture
q=queue.Queue()
def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


#Using command line arguments for determining what languages to use
from_code = sys.argv[1]
to_code = sys.argv[2]


#dictionary that stores the lang codes (used for lang codes that don't match between vosk and argos)
#vosk lang codes as the key, and argos/libre lang codes as the value 

vosk_langs = {"en", "es", "fr", "ar", "cn", "pt", "ar", "fa", "hi"}
translate_langs = {"en", "es", "fr", "ar", "zh", "pt", "ar", "fa", "hi"}

#vosk lang codes as the key
vosk_lang_map = {
    "en" : "en", 
    "es" : "es", 
    "fr" : "fr", 
    "ar" : "ar", 
    "cn" : "zh", 
    "pt" : "pt", 
    "ar" : "ar", 
    "fa" : "fa", 
    "hi" : "hi", 
}

argos_lang_map = {value: key for key, value in vosk_lang_map.items()}

#Getting microphone info
device = None
audio_input = sounddevice.query_devices(device, kind="input")
sample_rate = audio_input["default_samplerate"]

#Constants for audio data capture
BLOCK_SIZE = 10000
CHANNELS = 1

#Initalizing vosk model
lang = from_code if from_code in vosk_langs else argos_lang_map.get(from_code)
model = Model(lang=lang)

#Initalizing vosk recognizer
recognizer = KaldiRecognizer(model, sample_rate)

#Initializing the display 
display = OLEDDisplay(font_size = 15)

#Initializing translator API
translator = LibreTranslateAPI("https://translate.terraprint.co/")

prev_idx = 0
with sounddevice.RawInputStream(samplerate=sample_rate, blocksize=BLOCK_SIZE,dtype="int16",callback=callback,channels=CHANNELS):
     print("############## START ############## ")
     display.displayWord("*** START ***") 
     while True:
        data = q.get()
        if recognizer.AcceptWaveform(data):
            previous_words_idx = 0
            final_result = json.loads(recognizer.FinalResult())
            words = final_result.get("text")

            if len(words) > 0 :        
                print("**** ENTERED TRANSLATION *** ")
                src = from_code if from_code in translate_langs else vosk_lang_map.get(from_code)
                dst = to_code if to_code in translate_langs else vosk_lang_map.get(to_code)
                translated = translator.translate(q=words, source=src, target=dst)
                print(translated)
                display.displayWords(translated.split(" "))
                

            #print(final_result)
        else: 
            partial_result = json.loads(recognizer.PartialResult())
            print(partial_result.get("partial"))
            '''
            if len(partial_result.get("partial")) > 0:
                words = partial_result.get("partial").split(" ")
                new_start_idx = prev_idx
                new_end_idx = len(words)
                new_words = words[new_start_idx:new_end_idx+1]
                prev_idx = len(words) - 1
                display.displayWords(new_words)
                #print("words: ") 
                #print(words) 
                print(new_words)
            ''' 
