#import game_data
from game_data import TITLE, display_line, Hangman

print(TITLE)
display_line()

player = input("Pdlease, enter your name: ")

hangman = Hangman(player)
hangman.play()
