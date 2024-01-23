import sounddevice 
import queue
import queue 
import sys
import json
from vosk import Model, KaldiRecognizer
from display import OLEDDisplay

class Transcriber:
    def __init__(self, language, sample_rate, audio_block_size, audio_channels, audio_data_type):
        #Specifing audio capture data
        self.sample_rate = sample_rate
        self.BLOCK_SIZE = audio_block_size
        self.CHANNELS = audio_channels
        self.dtype = audio_data_type
        self.queue = queue.Queue()
        
        #Initializing speech model and recognizer
        self.model = Model(lang=language)
        self.recognizer = KaldiRecognizer(self.model, sample_rate)

        #initialize display
        self.display = OLEDDisplay(font_size = 15)

    #setting up call back for continous audio capture
    def __callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        queue.put(bytes(indata))


    def run(self):
        with sounddevice.RawInputStream(samplerate=self.sample_rate, blocksize=self.BLOCK_SIZE,dtype="int16",callback=self.__callback,channels=self.CHANNELS):
            print("############## START ############## ")
            self.display.displayWord("*** START ***") 
            while True:
                data = self.queue.get()
                if self.recognizer.AcceptWaveform(data):
                    words = json.loads(self.recognizer.FinalResult()).get("text")
                    print(words)