import random

def hello():
    return "Hello! I'm alice."


phrases = [
    "Hello my dear!",
    "I'm alice.",
    "I'm an artificial intelligence.",
    "How are you?",
    "I'm fine.",
    "I love computer science.",
]

def random_phrase():
    return phrases[random.randint(0, len(phrases)-1)]

