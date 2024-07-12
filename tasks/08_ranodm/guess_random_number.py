import random

random_number = random.randint(1,10)

print("Welcome to random number guessing program")
while True:
    user_guess = int(input("Guess random value :"))
    if user_guess == random_number:
        print("congrats!, your guess was correct.")
        break;
    elif user_guess > random_number:
        print("High value! Try again..")
    else:
        print("Low value! Try again..")
