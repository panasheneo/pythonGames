import random

number = random.randint(1, 10)
guess = None
guess_count = 0

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while guess != number:
    guess = int(input("Enter your guess: "))
    guess_count += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations, you guessed it in {guess_count} tries!")
