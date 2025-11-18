import random

target = random.randint(0, 10)
print("guess a number between o and 10")

try:
    guess = int(input("enter your guess: "))
    if guess== target:
        print("number match! you guesssed correctly")
    elif guess>target:
        print("your guess is too high.")
    else:
        print("your guess is too low.")
        print("correct number was:", target)
except ValueError:
        print("error: please enter a valid number !")