import random

# List of Manchester United players
players = [
    "Tom Heaton", "Victor Lindelöf", "Harry Maguire", "Luke Shaw",
    "Aaron Wan-Bissaka", "Christian Eriksen", "Casemiro",
    "Raphaël Varane", "Diogo Dalot", "Bruno Fernandes", "Scott McTominay",
    "Mason Mount", "Anthony Martial", "Marcus Rashford", "Antony",
    "Amad Diallo", "Shola Shoretire", "Alejandro Garnacho",
    "Rasmus Højlund"
    # Add more players here...
]

# Select a random player name
target_player = random.choice(players).upper()

# Initialize the guessed word with underscores
guessed_word = "_" * len(target_player)

# Track guessed letters
guessed_letters = set()

# Function to check if a letter is in the target word
def check_letter(letter):
    return letter in target_player

# Function to update the guessed word
def update_guessed_word(letter):
    global guessed_word
    for i, char in enumerate(target_player):
        if char == letter:
            guessed_word = guessed_word[:i] + letter + guessed_word[i+1:]

# Main game loop
while "_" in guessed_word:
    guess = input(f"Guess a letter: {guessed_word} ").upper()

    if guess in guessed_letters:
        print("You already guessed that letter!")
    else:
        guessed_letters.add(guess)
        if check_letter(guess):
            update_guessed_word(guess)
            print(f"Correct! {guessed_word}")
        else:
            print("Incorrect guess!")

print(f"Congratulations! You guessed the player: {target_player}")


