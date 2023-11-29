import sounddevice
import sys
import queue
import json
import time
from libretranslatepy import LibreTranslateAPI
from vosk import Model, KaldiRecognizer
from display import OLEDDisplay


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
print(device)

#Constants for audio data capture
BLOCK_SIZE = 10000
CHANNELS = 1

#Initalizing vosk model
model = Model(lang=from_code)

#Initalizing vosk recognizer
recognizer = KaldiRecognizer(model, sample_rate)

#Initializing the display 
display = OLEDDisplay(font_size = 15)

#Initializing translator API
translator = LibreTranslateAPI("https://translate.argosopentech.com/")


previous_num_of_word = 0
#print(audio_input)
with sounddevice.RawInputStream(samplerate=sample_rate, blocksize=BLOCK_SIZE,dtype="int16",callback=callback,channels=CHANNELS):
     print("############## START ############## ")
     while True:
        data = q.get()
        if recognizer.AcceptWaveform(data):
            previous_num_of_word = 0
            final_result = json.loads(recognizer.FinalResult())
            print(final_result)
        else: 
            partial_result = json.loads(recognizer.PartialResult())
            words = partial_result.get("partial").split(" ") 
            previous_num_of_word += len(words)
            num_of_words_to_dispay = len(words) - previous_num_of_word
            for i in range(num_of_words_to_dispay):
                display.displayWord(words[i])
            
               