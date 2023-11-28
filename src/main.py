import sounddevice
import sys
import queue
import json
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
#translator = LibreTranslateAPI("https://translate.argosopentech.com/")

#print(audio_input)
with sounddevice.RawInputStream(samplerate=sample_rate, blocksize=BLOCK_SIZE,dtype="int16",callback=callback,channels=CHANNELS):
     print("############## START ############## ")
     while True:
        data = q.get()
        if recognizer.AcceptWaveform(data):
            final_result = json.loads(recognizer.FinalResult())
            #ranslated = translator.translate(partial_result.get("partial", ""), from_code, to_code)
            print(final_result)
        else: 
            partial_result = json.loads(recognizer.PartialResult())
            if len(partial_result.get("partial")) > 0:
                words = partial_result.get("partial").split(' ')
                display.displayWord(words[-1])
                print(words[-1])
               