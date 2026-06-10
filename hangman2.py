import random #to pick random word from list
print("The game is related to IT field so wording will be accordingly")
words = ["python", "script", "coding", "syntax", "hacker", "cybersecurity", "hack", "javascript", "HTTP", "protocol"] #list of words


word = random.choice(words) 
guessed_letters = []  #list to track the guessed word
attempts = 6

while attempts > 0:
    display_list = []
    
    for char in word:
        if char in guessed_letters:
            display_list.append(char)
        else:
            display_list.append("_")
            
    display_string = " ".join(display_list)
    print("\nWord: " + display_string)
    
    if "_" not in display_list:
        print("You won! The word was " + word)
        break
        
    print("Attempts remaining: " + str(attempts))
    guess = input("Guess a letter: ").lower()
    
    #for exactly one character input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            print("Incorrect guess.")

if attempts == 0:
    print("\nGame over. The word was " + word)
