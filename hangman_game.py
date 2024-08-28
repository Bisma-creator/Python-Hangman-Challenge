import random 

def display_current_state(current_State):
    print(' '.join(current_State))

def init_state_with_reveal_letters(words, num_revealed = 3):
    """ initialize the state with all underscores"""
    current_State = ['_'] * len(words) #initialize with underscores

    """ Randomly select indices to reveal """
    indices_to_reveal = random.sample(range(len(words)), num_revealed)

    """ Place the revealed letters in their correct position"""
    for index in indices_to_reveal:
        current_State[index] = words[index]
        
    return current_State

def update_current_state(words, current_State, guess):
    """ update the current state after the player correct guess """
    for index, letter in enumerate(words):
        if letter.lower() == guess:
            current_State[index] = letter #preserve the correct letter case

""" main game setup """

words = ["Python", "Programming", "Object Oriented", "Vs Code", "Algorithm", "iteration", "Encapsulation"]
selected_word = random.choice(words)

""" initialized the state with some letters """ 
current_State = init_state_with_reveal_letters(selected_word)

""" set the number of allowed incorect attempts """
max_attempts = 6
attempts_left = max_attempts 

""" GAME LOOP """ 

while '_' in current_State and attempts_left > 0:
    print(f"Attempts Left: {attempts_left}\n")
    display_current_state(current_State)

    guess = input("Guess a letter to complete the word: ").lower().strip()

    if len(guess) == 1 and guess.isalpha():

        if guess in selected_word.lower(): #Convert the word o lower case for comparision
            update_current_state(selected_word, current_State, guess)
        else:
            attempts_left -= 1 #Decrement the attempts by 1 for an incorrect guess
            print(f"Incorrect Guess! You have '{attempts_left}'attempts left.")

    else:
        print("Enter a Valid Single letter, Please!")

    if '_' not in current_State:
        print("Congratulation! You've Guessed the word!")
        break
    elif attempts_left == 0:
        print(f"You have 0 attempts left! The word was '{selected_word}'. Better luck next time!")

# display_current_state(current_State)

