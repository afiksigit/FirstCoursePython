# Define constants

HANGMAN_PHOTOS = {
    0: '''
        x-------x
        ''',
    1: '''
        x-------x
        |
        |
        |
        |
        |
        ''',
    2: '''
        x-------x
        |       |
        |       0
        |
        |
        |
        ''',
    3: '''
        x-------x
        |       |
        |       0
        |       |
        |
        |
        ''',
    4: '''
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        ''',
    5: '''
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        ''',
    6: '''
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        '''
}

MAX_TRIES = 6


# Define the menu function which prints a welcome message and the number of attempts allowed
def menu():
    """
    Prints a welcome message and the number of attempts allowed.
    Parameters:
    None

    Returns:
    None
    """
    welcome_sentence = """Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""
    print(welcome_sentence, "\n", "attempts:", MAX_TRIES)


# Define the show_hidden_word function which shows the current state of the secret word with underscores and
# correctly guessed letters
def show_hidden_word(secret_word, old_letters_guessed):
    """
    Shows the current state of the secret word with underscores and correctly guessed letters.
    Parameters:
    secret_word (str): The secret word that the player is trying to guess.
    old_letters_guessed (list): A list of letters that the player has already guessed.

    Returns:
    str: The current state of the secret word with underscores and correctly guessed letters.
    """
    hidden_word = ''
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter + ' '
        else:
            hidden_word += '_ '
    return hidden_word


# Define the check_win function which checks if the player has correctly guessed the secret word
def check_win(secret_word, old_letters_guessed):
    """
    Checks if the player has correctly guessed the secret word.
    Parameters:
    secret_word (str): The secret word that the player is trying to guess.
    old_letters_guessed (list): A list of letters that the player has already guessed.

    Returns:
    bool: True if the player has correctly guessed the secret word, False otherwise.
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


# Define the check_valid_input function which checks if the player's input is valid
def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if the player's input is valid.
    Parameters:
    letter_guessed (str): The letter that the player has guessed.
    old_letters_guessed (list): A list of letters that the player has already guessed.

    Returns:
    bool: True if the player's input is valid, False otherwise.
    """
    return (len(letter_guessed)) == 1 and (letter_guessed.isalpha() and letter_guessed not in old_letters_guessed)


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Updates the list of guessed letters and prints an error message if the input is invalid.
    Parameters:
    letter_guessed (str): The letter that the player has guessed.
    old_letters_guessed (list): A list of letters that the player has already guessed.

    Returns:
    bool: True if the letter has been successfully added to the list of guessed letters, False otherwise.
    """

    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    old_letters_guessed = "->".join(sorted(old_letters_guessed))
    print('X\n', old_letters_guessed)
    return False


def choose_word(file_path, index):
    try:
        with open(str(file_path), 'r') as file:
            # read the file contents and split into individual words
            words = file.read().split()

            # count the number of unique words in the file
            unique_words = set(words)
            num_unique_words = len(unique_words)

            # find the word at the specified index
            num_words = len(words)
            index = (index - 1) % num_words  # handle circular indexing
            secret_word = words[index]
            return secret_word, num_unique_words
    except Exception as e:
        print(e)



def initially_input():
    path = input("Please enter the  PATH of the file: ")
    index = int(input("Also enter the INDEX of the word inside the file: "))
    return path, index;


def char_input():
    char = input("Guess char: ")
    return char


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


def is_letter_in_secret_word(letter, secret_word):
    return letter in secret_word


def validate_guessed_letter(letter_guessed, old_letters_guessed):
    while not try_update_letter_guessed(letter_guessed, old_letters_guessed):
        print("CHAR NOT VALLID...")
        letter_guessed = char_input()


def main():
    num_of_tries = 0
    old_letters_guessed = []

    # Display the menu and get the secret word
    menu()
    path, secret_word_index = initially_input()
    secret_word, secret_word_amount = choose_word(path, secret_word_index)

    # Display the hangman for the initial state
    print_hangman(num_of_tries)

    # Loop until the user wins or loses
    while not check_win(secret_word, old_letters_guessed) and num_of_tries < MAX_TRIES:
        # Get a valid guessed letter from the user and update the list of old letters guessed
        letter_guessed = char_input()
        validate_guessed_letter(letter_guessed, old_letters_guessed)

        # Check if the guessed letter is in the secret word, display the updated hidden word, and update number of
        # tries and hangman if necessary

        guess_result = is_letter_in_secret_word(letter_guessed, secret_word)
        hidden_word = show_hidden_word(secret_word, old_letters_guessed)
        print(hidden_word)
        if not guess_result:
            num_of_tries += 1
            print(f"You failed {num_of_tries} times")
            print_hangman(num_of_tries)

    # Print win or lose message based on the number of tries
    if num_of_tries < MAX_TRIES:
        print("WIN")
    else:
        print("LOSE")


if __name__ == '__main__':
    main()
