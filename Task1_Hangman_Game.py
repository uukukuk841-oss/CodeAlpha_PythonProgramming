import random

WORDS = ["python", "student", "computer", "program", "internship"]
MAX_WRONG_GUESSES = 6


def display_word(word, guessed_letters):
    """Return the word with unguessed letters hidden."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("=" * 40)
    print("           HANGMAN GAME")
    print("=" * 40)
    print(f"Guess the word. You can make {MAX_WRONG_GUESSES} incorrect guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("\nWord:", display_word(secret_word, guessed_letters))
        print(f"Incorrect guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("That letter is not in the word.")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            return

    print(f"\nGame over! The correct word was: {secret_word}")


if __name__ == "__main__":
    play_game()
