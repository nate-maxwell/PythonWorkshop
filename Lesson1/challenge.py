import random

answer = random.randint(1, 100)
guess = 0
attempts = 0

print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it in 8 tries or less?")

while guess != answer:
    if attempts >= 8:
        print("Sorry, too many tries! Game over!")
        print("The secret number was", answer, "!")
        break

    guess = input("New guess: ")
    attempts += 1

    if int(guess) > answer:
        print("Nope, too high...")
    elif int(guess) < answer:
        print("Nope, too low...")
    else:
        print("Congratulations, you got it!")
        break
