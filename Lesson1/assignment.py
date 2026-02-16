import random

answer = random.randint(1, 100)
guess = 0

print("I'm thinking of a number between 1 and 100. Can you guess what it?")

while guess != answer:
    guess = input("New guess: ")

    if int(guess) > answer:
        print("Nope, too high...")
    elif int(guess) < answer:
        print("Nope, too low...")
    else:
        print("Congratulations, you got it!")
        break
