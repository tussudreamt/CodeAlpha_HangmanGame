import tkinter as tk
import random

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("400x400")
        
        # Game state variables
        self.words = ["python", "script", "coding", "syntax", "hacker", "cybersecurity", "hack", "javascript", "HTTP", "protocol"]
        self.word = ""
        self.guessed_letters = []
        self.attempts = 6
        
        # --- UI Elements ---
        
        # Displays the word with underscores
        self.word_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=30)
        
        # Displays attempts remaining
        self.info_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.info_label.pack(pady=5)
        
        # Text box for the player to type a letter
        self.entry = tk.Entry(root, font=("Helvetica", 18), width=5, justify='center')
        self.entry.pack(pady=10)
        # Allows pressing the "Enter" key to submit a guess
        self.root.bind('<Return>', lambda event: self.guess_letter())
        
        # Button to submit the guess
        self.guess_button = tk.Button(root, text="Guess", command=self.guess_letter, font=("Helvetica", 12))
        self.guess_button.pack(pady=5)
        
        # Label to show errors, warnings, or win/loss messages
        self.message_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.message_label.pack(pady=15)
        
        # Button to restart the game
        self.reset_button = tk.Button(root, text="Restart Game", command=self.start_game, font=("Helvetica", 10))
        self.reset_button.pack(pady=10)
        
        # Start the first game automatically
        self.start_game()

    def start_game(self):
        """Resets the game state for a new round."""
        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.attempts = 6
        
        # Reset UI elements
        self.message_label.config(text="")
        self.entry.config(state='normal')
        self.guess_button.config(state='normal')
        self.update_ui()

    def update_ui(self):
        """Updates the word display and the attempts counter."""
        display_list = []
        for char in self.word:
            if char in self.guessed_letters:
                display_list.append(char)
            else:
                display_list.append("_")
                
        self.word_label.config(text=" ".join(display_list))
        self.info_label.config(text="Attempts remaining: " + str(self.attempts))

    def guess_letter(self):
        """Processes the player's input from the text box."""
        # Get the letter and immediately clear the entry box
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        
        # Validation checks
        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Invalid input. Enter a single letter.", fg="red")
            return
            
        if guess in self.guessed_letters:
            self.message_label.config(text="You already guessed that letter.", fg="orange")
            return
            
        # Process a valid, new guess
        self.guessed_letters.append(guess)
        
        if guess not in self.word:
            self.attempts -= 1
            self.message_label.config(text="Incorrect guess.", fg="red")
        else:
            self.message_label.config(text="Good guess!", fg="green")
            
        self.update_ui()
        self.check_game_over()

    def check_game_over(self):
        """Checks if the player has won or lost the game."""
        # Check for a win (no more underscores needed)
        won = True
        for char in self.word:
            if char not in self.guessed_letters:
                won = False
                break
                
        if won:
            self.message_label.config(text="You won! The word was " + self.word, fg="green")
            self.end_game()
        # Check for a loss (0 attempts left)
        elif self.attempts == 0:
            self.message_label.config(text="Game over. The word was " + self.word, fg="red")
            self.end_game()

    def end_game(self):
        """Disables the input fields when the game ends."""
        self.entry.config(state='disabled')
        self.guess_button.config(state='disabled')

# --- Run the Application ---
if __name__ == "__main__":
    # Create the main window and start the GUI application
    main_window = tk.Tk()
    app = HangmanGUI(main_window)
    main_window.mainloop()
