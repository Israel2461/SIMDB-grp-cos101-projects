yoruba_Lang = {
    "omo": "child",
    "ile": "house",
    "omi": "water",
    "owo": "money",
    "ounje": "food",
    "aso": "clothes",
    "ile-iwe": "school",
    "oluko": "teacher",
    "akoko": "time",
    "ojo": "day",
    "orun": "sun",
    "osupa": "moon",
    "ife": "love",
    "ore": "friend",
    "iya": "mother",
    "baba": "father",
    "oko": "farm",
    "aja": "dog",
    "ologbo": "cat",
    "ise": "work",
}


def translate(word):
    translation = yoruba_Lang.get(word.lower())
    if translation:
        return f"{word.capitalize()} means {translation}."
    else:
        return f"Sorry, {word.capitalize()} is not in the dictionary."