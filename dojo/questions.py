import random

questions = [
    {"question": "2 + 2", "answer": "4"},
    {"question": "3 + 5", "answer": "8"},
    {"question": "10 - 7", "answer": "3"},
    {"question": "6 * 2", "answer": "12"},
    {"question": "9 / 3", "answer": "3"},
    {"question": "5 + 5", "answer": "10"},
    {"question": "7 - 2", "answer": "5"},
    {"question": "8 + 1", "answer": "9"},
    {"question": "4 * 3", "answer": "12"},
    {"question": "12 / 4", "answer": "3"},
]

def get_random_question():
    return random.choice(questions)