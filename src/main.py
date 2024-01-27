import sys
from transcription import Transcriber

def transcribe(language):
    transcriber = Transcriber(language=language)
    transcriber.run()
    return

def translate(from_code, to_code):
    return

#Read cmd arguements 
mode = sys.argv[1]
if mode == '-c':
    language = sys.argv[2]
    transcribe(language=language)
    exit()
else: 
    from_code = sys.argv[1]
    to_code = sys.argv[2]
    if from_code == to_code:
        transcribe(language=from_code)
        exit()
    translate(from_code=from_code, to_code=to_code)