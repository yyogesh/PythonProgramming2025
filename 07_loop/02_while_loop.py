import random

secret_number = random.randint(1, 100) #51
attempts = 0
max_attempts = 10

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")


while attempts < max_attempts:
    guess = int(input("Guess the number: ")) #20
    attempts += 1

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        attempts -= 1
    elif guess < secret_number:  # true
       print(f"Too low! Attempts remaining: {max_attempts - attempts}")
    elif guess > secret_number:
        print(f"Too high! Attempts remaining: {max_attempts - attempts}")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

if attempts >= max_attempts:
    print(f"\nGame Over! The number was {secret_number}")