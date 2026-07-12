import random

# List of words
words = ["python", "robot", "apple", "coding", "laptop"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("=================================")
print("      WELCOME TO HANGMAN")
print("=================================")

while attempts > 0:

    # Display the word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Attempts Left:", attempts)

    # Check if player has won
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong guess!")

# If player loses
if attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", word)
    