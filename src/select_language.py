from button import ButtonListener
import faulthandler

faulthandler.enable()
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
        print(idx)
        if x[0] == 3: #MOVE TO THE RIGHT
            idx = (idx + 1) % len(langs)
        elif x[0] == 2: #MOVE TO THE LEFT
            idx = (idx - 1) % len(langs)
        elif x[0] == 1:
            selected = True
            lang = langs[idx]
    return lang

def select_to_language():
    return



buttons = ButtonListener()
a = select_from_language(buttons)
print(a)