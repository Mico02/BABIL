from button import ButtonHandler, PowerButtonHandler
from display import OLEDDisplay
import sys
import threading
import subprocess

caption_languages = {"en" : "English",
                     "cn" : "Chinese", 
                     "ru" : "Russian", 
                     "fr" : "French", 
                     "de" : "German", 
                     "es" : "Spanish", 
                     "pt" : "Portuguese", 
                     "gr" : "Greek", 
                     "tr" : "Turkish", 
                     "vn" : "Vietnamese ", 
                     "it" : "Italian", 
                     "nl" : "Dutch",
                     "ar" : "Arabic",
                     "ca" : "Catalan",
                     "fa" : "Farsi",
                     "ph" : "Filipino",
                     "uk" : "Ukrainian",
                     "kz" : "Kazakh",
                     "sv" : "Swedish",
                     "jp" : "Japanese",
                     "eo" : "Esparanto",
                     "hi" : "Hindi",
                     "cs" : "Czech",
                     "po" : "Polish",
                     "uz" : "Uzbek",
                     "ko" : "Korean",
                     "br" : "Breton",
                     "gu" : "Gujarati"} 

    

def select_device_mode(buttons: ButtonHandler, display: OLEDDisplay):
    modes = ["Captioning", "Translation"]
    selected = False
    option = [0]
    idx = 0
    while not selected:
        display.displayWord(modes[idx])
        buttons.selectOption(option)
        if option[0] == ButtonHandler.RIGHT:
            idx = (idx + 1) % len(modes)
        elif option[0] == ButtonHandler.LEFT:
            idx = (idx - 1) % len(modes)
        elif option[0] == ButtonHandler.SELECT:
            selected = True
        else:
            print("Error: invalid button", file=sys.err)
    return modes[idx]

def select_language(buttons: ButtonHandler, languages: dict, display: OLEDDisplay):
    idx = 0
    selected = False
    x = [0]
    lang_list = list(languages)
    while not selected: 
        display.displayWord(languages.get(lang_list[idx]))
        buttons.selectOption(x)
        if x[0] == ButtonHandler.RIGHT: #MOVE TO THE RIGHT
            idx = (idx + 1) % len(languages)
        elif x[0] == ButtonHandler.LEFT: #MOVE TO THE LEFT
            idx = (idx - 1) % len(languages)
        elif x[0] == ButtonHandler.SELECT:
            selected = True
        else:
            print("Error: invalid button", file=sys.err)
    return lang_list[idx]


powerButton = PowerButtonHandler()
buttons = ButtonHandler()
powerButtonThread = threading.Thread(target=powerButton.wait_for_press)
powerButtonThread.start()

display = OLEDDisplay(font_size=15)

mode = select_device_mode(buttons,display)
print(f"{mode} is the selected mode")
if mode == "Captioning":
    lang = select_language(buttons, caption_languages,display)
    print(f"{caption_languages.get(lang)} is the selected lang")
    powerButton.stop_waiting()
    powerButtonThread.join()
    subprocess.Popen(["python3" ,"src/main.py","-c",lang])
    print("GOODBYE")
    exit()



