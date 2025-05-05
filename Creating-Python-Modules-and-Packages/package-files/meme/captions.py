import random

meme_captions = [
    "When you realize it's Monday again...",
    "I don't always test my code, but when I do, I do it in production.",
    "That feeling when you fix a bug at 3 AM.",
    "Code so clean, you could eat off it.",
    "Debugging: Removing the needles from the haystack.",
]

def get_random_caption():
    return random.choice(meme_captions)
