import random

sectors = {
    "Technology": ["PYTHON", "ALGORITHM", "DATABASE", "NETWORK"],
    "Finance": ["INVESTMENT", "EQUITY", "DIVIDEND", "PORTFOLIO"],
    "Healthcare": ["HOSPITAL", "DIAGNOSIS", "VACCINE", "SURGERY"],
    "Space": ["GALAXY", "ORBIT", "SATELLITE", "GRAVITY"]
}

def play_game():
    category = random.choice(list(sectors.keys()))
    word = random.choice(sectors[category]) 
    
    guessed_letters = []
    attempts = 6

    print("\n                NEW GAME             ")
    print("\n ")
    print(f"Clue: This word is related to the '{category}' sector.")
    print("Guess one letter at a time!")

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        
        display = ""
        for char in word:
            if char in guessed_letters:
                display += char + " "
            else:
                display += "_ "
        
        print(display.strip())

        if "_" not in display:
            print(f"\nCongratulations! You won! The word was {word}")
            return

        guess = input("Guess a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid Input: Please enter exactly one letter.")
            continue
        
        if guess in guessed_letters:
            print("Already Guessed: You already tried that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1

    print(f"\nGame Over! You lost! The word was {word}")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (Y/N): ").upper()
        if play_again != "Y":
            break
