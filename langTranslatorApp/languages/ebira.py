ebira_Lang = {
    "joy" : "Iraje",
    "heaven" : "Eku’oiza",
    "dance" : "Ézéé",
    "money" : "Ekehi",
    "happy" : "Ayohine",
    "light" : "ira",
    "time" : "úmè",
    "sleep" : "ara",
    "morning" : "Enene",
    "water" : "ényí",
    "chair" : "aga",
    "night" : "irahu",
    "house" : "irehi",
    "strong" : "ùvèchì",
    "learn" : "òyìkòsè",
    "no" : "Hèyìyè",
    "we" : "Eyyi",
    "but" : "ààmaá",
    "correct" : "oojiri",
    "song" : "àhè"
}

def translate(word):
    translation = ebira_Lang.get(word.lower())
    if translation:
        return f"{word.capitalize()} means {translation}."
    else:
        return f"Sorry, {word.capitalize()} is not in the dictionary."