"""A number-guessing game."""

# Put your code here

from random import randint

tries = 0 
number = randint (1,100)

name = input("What's your name? \n")

print(f'{name}, I am thinking of a number between 1 and 100 \n Can you guess what number it is?')


while True: 
    guess = input('Your guess?')

    # Verify the guess is a number 
    try:
        guess = int(guess)
    except ValueError:
        print ("{guess} is not a valid number, try again." )    
        continue

    #Verify guess is between 1 and 100

    if guess < 1 and guess > 100:
        print ('Please guess a number between 1 and 100')
        continue
    tries += 1 
    if guess < number:
        print('Your guess is too low, try again.')
    elif guess > number:
        print('Your guess is too high, try again.')
    else: 
        print (f'Well done, {name}!')
        print(f'Your found my number in {tries} tries!')