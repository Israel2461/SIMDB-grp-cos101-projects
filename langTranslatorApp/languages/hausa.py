hausa_Lang = {

    "hello": "sannu",
    "goodbye": "sai an jima",
    "thank you": "na gode",
    "please": "don Allah",
    "yes": "eh",
    "no": "a'a",
    "man": "namiji",
    "woman": "mace",
    "child": "yaro",
    "food": "abinci",
    "water": "ruwa",
    "house": "gida",
    "school": "makaranta",
    "teacher": "malami",
    "student": "dalibi",
    "book": "littafi",
    "money": "kudi",
    "friend": "aboki",
    "love": "so",
    "work": "aiki"

}

def translate(word):
    translation = hausa_Lang.get(word.lower())
    if translation:
        return f"{word.capitalize()} means {translation}."
    else:
        return f"Sorry, {word.capitalize()} is not in the dictionary."