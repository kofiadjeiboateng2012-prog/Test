print("===== Welcome to the Number Guessing Game! =====")
total_attempts = 5
used_attempts = 0
secret_number = 67
while used_attempts < total_attempts:
    guess = int(input("Enter your guess: "))
    used_attempts += 1
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low! the number is higher.")
    else:
        print("Too high! the number is lower .")
else:
    print("Game over! You ran out of attempts.")
