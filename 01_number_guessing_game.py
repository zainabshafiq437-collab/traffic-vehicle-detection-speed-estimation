import random
secret_number = random.randint(1, 100)
attempts = 0
print("--- Number Guessing Game ---")
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == secret_number:
        print(f"You WIN! in {attempts} tries!")
        break
    elif guess > secret_number:
        print(f"{guess} is too HIGH!")
    else:
        print(f"{guess} is too LOW!")
    if attempts == 5:
        print(f"Game Over! Number was {secret_number}")
        break
