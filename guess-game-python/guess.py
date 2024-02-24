import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the number of guesses allowed
num_guesses = 7

# Print welcome message
print("Welcome to the 'Guess the Number' game!")
print("You have", num_guesses, "guesses to find the secret number between 1 and 100.")

# Start the game loop
while num_guesses > 0:
    # Get the player's guess
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue  # Skip to the next iteration if the input is invalid

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        break  # Exit the loop if the guess is correct

    # Give feedback based on the guess
    if guess < secret_number:
        print("Your guess is too low. Try again.")
        num_guesses -= 1  # Decrement the remaining guesses
    else:
        print("Your guess is too high. Try again.")
        num_guesses -= 1  # Decrement the remaining guesses

# Handle the case where the player runs out of guesses
if num_guesses == 0:
    print("Sorry, you ran out of guesses. The secret number was", secret_number)

print("Thanks for playing!")