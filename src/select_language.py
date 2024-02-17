from button import ButtonHandler, PowerButtonHandler
import threading

from_langs = {"en" : "English",
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
              "gu" : "Gujarati",} 

translation_map = {"en"}
    
def select_from_language(buttons):
    idx = 0
    selected = False
    lang = ""
    langs = list(from_langs)
    x = [10]
    while not selected: 
        buttons.selectOption(x)
        print(from_langs.get(langs[idx]), end=" ")
        if x[0] == ButtonHandler.RIGHT: #MOVE TO THE RIGHT
            idx = (idx + 1) % len(langs)
        elif x[0] == ButtonHandler.LEFT: #MOVE TO THE LEFT
            idx = (idx - 1) % len(langs)
        elif x[0] == ButtonHandler.SELECT:
            selected = True
            lang = langs[idx]
        print(idx)
    return lang

def select_to_language():
    return

powerButton = PowerButtonHandler()
buttons = ButtonHandler()


powerButtonThread = threading.Thread(target=powerButton.wait_for_press)
powerButtonThread.start()
a = select_from_language(buttons)
print(a)
powerButton.stop_waiting()
powerButtonThread.join()