import sys
from transcription import Transcriber
from display import OLEDDisplay

def transcribe(language, display):
    transcriber = Transcriber(language=language, display=display)
    transcriber.run()
    return

def translate(from_code, to_code):
    return

#Initializing display object
display = OLEDDisplay(font_size=15)

#Read cmd arguements 
mode = sys.argv[1]
if mode == '-c':
    language = sys.argv[2]
    transcribe(language,display)
    exit()
else: 
    from_code = sys.argv[1]
    to_code = sys.argv[2]
    if from_code == to_code:
        transcribe(language=from_code)
        exit()
    translate(from_code=from_code, to_code=to_code)