import random

print('--------------------------------')
print('        GUESS THE NUMBER')
print('--------------------------------')
print()

the_number = random.randint(0, 100)
guess = int(-1)
name = input("Player what is your name? ")

while guess != the_number:
    guess_text = input('Guess the number (0 - 100):  ')
    guess = int(guess_text)
    if guess > the_number:
            print('Sorry {0}, your guess of {1} was too high. :('.format(name, guess))
    elif guess < the_number:
            print('Sorry {0}, your guess of {1} was too low. :('.format(name, guess))
    else:
            print('Correct {0}, good work. It was {1}. :)'.format(name, guess))
