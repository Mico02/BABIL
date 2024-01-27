import sounddevice 
import queue
import queue 
import sys
import json
from vosk import Model, KaldiRecognizer

class Transcriber:
    def __init__(self, language, display, audio_block_size=10000, audio_channels=1, audio_data_type="int16"):
        #Specifing audio capture data
        #self.sample_rate = sample_rate
        self.__BLOCK_SIZE = audio_block_size
        self.__CHANNELS = audio_channels
        self.__dtype = audio_data_type
        self.__queue = queue.Queue()
        self.__display = display

        #Getting microphone information
        device = None
        self.sample_rate = sounddevice.query_devices(device, kind="input")["default_samplerate"]
        
        #Initializing speech model and recognizer
        self.model = Model(lang=language)
        self.recognizer = KaldiRecognizer(self.model, self.sample_rate)

    #setting up call back for continous audio capture
    def __callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        self.__queue.put(bytes(indata))

    def run(self):
        with sounddevice.RawInputStream(samplerate=self.sample_rate, blocksize=self.__BLOCK_SIZE,dtype=self.__dtype,callback=self.__callback,channels=self.__CHANNELS):
            print("############## START ############## ")
            self.__display.displayWord("*** START ***") 
            while True:
                data = self.__queue.get()
                if self.recognizer.AcceptWaveform(data):
                    words = json.loads(self.recognizer.FinalResult()).get("text").split(" ")
                    print(words)
                    self.__display.displayWords(words)
                else: 
                    partial_result = json.loads(self.recognizer.PartialResult())
                    #print(partial_result.get("partial"))