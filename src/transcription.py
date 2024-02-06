import sounddevice 
import queue
import queue 
import sys
import json
import time
import threading
from buttonlistener import start_listener
from vosk import Model, KaldiRecognizer

class Transcriber:
    def __init__(self, language, display, audio_block_size=10000, audio_channels=1, audio_data_type="int16"):
        #Initializing the button listener flag
        self.__exit_flag = [False]
        
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
            #Initializing button listener thread
            listener_thread = threading.Thread(target=start_listener,args=(self.__exit_flag,))
            listener_thread.start()

            new_word_starting_idx = 0
            shutdown_phrase = ["one", "two", "three", "stop"]
            print("############## START ############## ")
            self.__display.displayWord("* START *") 
            while True:
                if self.__exit_flag[0]:
                    self.__display.displayWord("*STOPPING*")
                    time.sleep(1)
                    self.__display.displayWord("")
                    exit()
                data = self.__queue.get()
                if self.recognizer.AcceptWaveform(data):
                    new_word_starting_idx = 0
                    words = json.loads(self.recognizer.FinalResult()).get("text")
                    #print(words)
                else: 
                    partial_result = json.loads(self.recognizer.PartialResult()).get("partial").split(" ")
                    partial_result = list(filter(None, partial_result))
                    new_words = partial_result[new_word_starting_idx::]
                    new_word_starting_idx = len(partial_result)
                    if len(partial_result) > 0 or len(new_words) > 0:
                        #print("Partial: ",end="")
                        #print(partial_result, end="")
                        #print("New: ",end="")
                        #print(new_words)
                        self.__display.displayWords(new_words)