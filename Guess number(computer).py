import random

def computer_guess(x):
    low=1
    high=x
    feedback=''

    while feedback!='c':
        guess=random.randint(low,high)
        feedback=input(f"Is {guess} to high(H) or too low(L) or correct(C)").lower()
        if feedback=='l':
            low=guess+1
        elif feedback=='h':
            high=guess-1
        elif feedback=="c":
            print("You are correct computer")

computer_guess(20)
