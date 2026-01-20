yoruba_Lang = {
    "child": "omo",
    "house": "ile",
    "water": "omi",
    "money": "owo",
    "food": "ounje",
    "clothes": "aso",
    "school": "ile-iwe",
    "teacher": "oluko",
    "time": "akoko",
    "day": "ojo",
    "sun": "orun",
    "moon": "osupa",
    "love": "ife",
    "friend": "ore",
    "mother": "iya",
    "father": "baba",
    "farm": "oko",
    "dog": "aja",
    "cat": "ologbo",
    "work": "ise"
}


def translate(word):
    translation = yoruba_Lang.get(word.lower())
    if translation:
        return f"{word.capitalize()} means {translation}."
    else:
        return f"Sorry, {word.capitalize()} is not in the dictionary."