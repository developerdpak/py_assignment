import random

SCREEN_SIZE = 60
TITLE= """
\
██    ██   ██████   ███   ██   ██████   ██    ██   ██████   ███   ██
██    ██  ██    ██  ████  ██  ██        ███  ███  ██    ██  ████  ██
████████  ████████  ██ ██ ██  ██  ████  ██ ██ ██  ████████  ██ ██ ██
██    ██  ██    ██  ██  ████  ██    ██  ██    ██  ██    ██  ██  ████
██    ██  ██    ██  ██   ███   ███████  ██    ██  ██    ██  ██   ███

"""

words={
    'COMPUTER',
    'PROGRAMMING',
    'INHERITANCE',
    'POLYMORPHISM',
    'DICTIONARY',
    'COMPREHENSION',
    'LAMBDA',
    'ITERATION',
}

greetings = [
    "We are so excited to have you on our team, {}!",
    "We are so thrilled to have yout at our terminal, {}!",
    "Welcome, {}!! Let's start the exciting game",
]

questions = [
        {
            'word': 'computer',
            'definition': 'An electronic device that is used for storing, and computing data in digital form.'
        },
        {
            'word': 'programming', 
            'definition': 'The process of instructing the computer todo certain task.'
        },
        {
            'word':
            'inheritance',
            'definition':
            'The process by which a child class takes a base from an another class to retain similar implementation'
        },
        {
            'word':
            'polymorphism',
            'definition':
            'The ability of a program in OOP that is able to show different characteristics in different situations'
        },
        {
            'word': 'dictionary',
            'definition': 'A data type in python that has key-value pair'
        },
        {
            'word': 'comprehension',
            'definition': 'A method of generating different collection data types based on another collection of data'
        },
        {
            'word': 'lambda',
            'definition': 'An anonymous function that is used as one liner function'
        },
        {
            'word':
            'iteration',
            'definition':
            'The method of running a sequence of instructions or code in a repeated manner '
            'until specific result is achieved'
        },
    ]


def display_line():
    print('=' * SCREEN_SIZE)

 
class Hangman:
    def __init__(self, player):
        self.player = player
        print(greetings[random.randint(0, len(greetings)-1)].format(self.player))
        display_line()

        print("Lets start with the word:\n")


    def play(self):
        current = questions[random.randint(0, len(questions)-1)]
        print(current['word'])
        print(current['definition'])




