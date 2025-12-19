igbo_Lang = {
    "water": "mmiri",
    "food": "nri",
    "spoon": "ngaji",
    "book": "akwukwo",
    "house": "ulo",
    "man": "nwoke",
    "woman": "nwanyi",
    "child": "nwa",
    "school": "ulo akwukwo",
    "road": "uzo",
    "market": "ahia",
    "money": "ego",
    "friend": "enyi",
    "family": "ezinaulo",
    "love": "ihunanya",
    "work": "oru",
    "sleep": "ura",
    "sun": "anyanwu",
    "moon": "onwa",
    "fire": "oku"
}


def translate(word):
    translation = igbo_Lang.get(word.lower())
    if translation:
        return f"{word.capitalize()} means {translation}."
    else:
        return f"Sorry, {word.capitalize()} is not in the dictionary."