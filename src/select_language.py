from button import ButtonListener
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
    while not selected:
        print(from_langs.get(langs[idx]))
        if x == '3': #MOVE TO THE RIGHT
            idx = (idx + 1) % len(langs)
        elif x == '2': #MOVE TO THE LEFT
            idx = (idx - 1) % len(langs)
        elif x == '1':
            selected = True
            lang = langs[idx]
    return lang

def select_to_language():
    return



buttons = ButtonListener()
a = select_from_language(b)
print(a)