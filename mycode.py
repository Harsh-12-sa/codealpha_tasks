import random

def choose_word():
    words = ['python', 'hangman', 'developer', 'programming', 'challenge', 'computer', 'keyboard']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def get_guess():
    # Simulating predefined guesses for non-interactive environments
    predefined_guesses = ['a', 'e', 'i', 'o', 'u', 's', 't', 'r', 'n', 'g']
    for guess in predefined_guesses:
        yield guess

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6
    guess_generator = get_guess()

    print("Welcome to Hangman!")
   
    while incorrect_guesses < max_attempts:
        print(display_word(word, guessed_letters))
       
        try:
            guess = next(guess_generator)
            print(f"Auto-guessing: {guess}")
        except StopIteration:
            print("No more guesses available.")
            break
       
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
       
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
       
        guessed_letters.add(guess)
       
        if guess not in word:
            incorrect_guesses += 1
            print(f"Incorrect guess! {max_attempts - incorrect_guesses} attempts left.")
       
        if set(word).issubset(guessed_letters):
            print(display_word(word, guessed_letters))
            print("Congratulations! You guessed the word.")
            return

    print(f"Game Over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()

