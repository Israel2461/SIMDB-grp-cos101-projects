calabar_Lang = {
    "joy" : "Utịñ",
    "heaven" : "Enyịn Abasi",
    "dance" : "Ikpọñ",
    "money" : "Ego",
    "happy" : "Utịñ idem",
    "light" : "Uforo",
    "time" : "Uforo edem",
    "sleep" : "Mbre",
    "morning" : "Mbre itie",
    "water" : "Mmọn",
    "chair" : "Akpa",
    "night" : "Mbubre",
    "house" : "Ufok",
    "strong" : "Ikpọn idem",
    "learn" : "Kụt",
    "no" : "Mma",
    "we" : "Anyin",
    "but" : "Ke",
    "correct" : "Mfo",
    "song" : "Ekong"
}

def translate(word):
    translation = calabar_Lang.get(word.lower())
    if translation:
        return f"{word.capitalize()} means {translation}."
    else:
        return f"Sorry, {word.capitalize()} is not in the dictionary."