import random

def guess(x):
    computer_choice=random.randint(1,x)
    guess=0

    while guess!=computer_choice:
        guess=int(input(f"Guess your number between 1 and {x}: "))
        if guess<computer_choice:
            print("Your number is too low")
        elif guess>computer_choice:
            print("Your number is too big")
        else:
            print("Congratulation,your guess is right!!")

guess(10)