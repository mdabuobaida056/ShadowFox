import random
# Hangman Game - Intermediate Task
# Word list
words = ["python", "developer", "internship", "shadowfox"]

# Random word selection
word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")

while attempts > 0:
    display_word = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    # Win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You won!")
        break

    guess = input("Enter a letter: ").lower()

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Wrong guess
    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess!")

# Lose condition
if attempts == 0:
    print("💀 Game Over! The word was:", word)
