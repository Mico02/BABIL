import sounddevice
import sys
import queue
import json
import time
import threading
#from libretranslatepy import LibreTranslateAPI
from vosk import Model, KaldiRecognizer
from display import OLEDDisplay
from googletrans import Translator



q=queue.Queue()
def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


#Using command line arguments for determining what languages to use
from_code = sys.argv[1]
to_code = sys.argv[2]

#Getting microphone info
device = None
audio_input = sounddevice.query_devices(device, kind="input")
sample_rate = audio_input["default_samplerate"]

#Constants for audio data capture
BLOCK_SIZE = 10000
CHANNELS = 1

path = r"/Users/mohamedhussein/Documents/Capstone/VoskModels/vosk-model-small-en-us-0.15"
#Initalizing vosk model
model = Model(path)

#Initalizing vosk recognizer
recognizer = KaldiRecognizer(model, sample_rate)

#Initializing the display 
#display = OLEDDisplay(font_size = 15)

#Initializing translator API
translator = LibreTranslateAPI("https://translate.argosopentech.com/")
translatergt = Translator()

def captureAudio():
    with sounddevice.RawInputStream(samplerate=sample_rate, blocksize=BLOCK_SIZE,dtype="int16",callback=callback,channels=CHANNELS):
        print("############## START ############## ")
        display.displayWord("*** START ***") 
        while True:
            pass

def translateAndDisplay():
    data = q.get()
     if recognizer.AcceptWaveform(data):
            previous_words_idx = 0
            final_result = json.loads(recognizer.FinalResult())
            words = final_result.get("text")
            if len(words) > 0 :        
                print("**** ENTERED TRANSLATION *** ")
                translated = translatergt.translate(text=words, src=from_code, dest=to_code)
                print(translated.text)
                display.displayWords(translated.text.split(" "))

transcribe_thread = threading.Thread(target=captureAudio)
translate_thread = threading.Thread(target=translateAndDisplay)

transcibe_thread.start()
translate_thread.start()






"""
prev_idx = 0
#print(audio_input)
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
                translated = translatergt.translate(text=words, src=from_code, dest=to_code)
                print(translated.text)
                display.displayWords(translated.text.split(" "))
                

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
"""