from vosk import Model

#Installs the speech recognition models in langs
langs = ["en", "es", "fr", "ar", "cn", "pt", "ar", "fa", "hi"]
for lang in langs:
    print(f"Downloading {lang} model...")
    model = Model(lang=lang)
    print(f"Downloaded {lang} model. \n")
    del model