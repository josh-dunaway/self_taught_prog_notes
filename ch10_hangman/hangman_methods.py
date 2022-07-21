from operator import truediv

def file_can_be_found(path: str) -> bool:
    import os
    if os.path.exists(path):
        return True
    return False

#should not be used for massive files - just those
#with a few hundred lines of text
def count_lines_in_txt_file(path: str) -> int:
    if(file_can_be_found(path)):
        with open(path, 'r') as f:
            num_lines = len(f.readlines())
        return num_lines
    return None

def get_random_line_from_file(path: str) -> str:
    num_lines = count_lines_in_txt_file(path)
    if num_lines == None:
        return None
    import random
    with open(path, 'r') as f:
        for i in range(random.randint(1, num_lines)):
            selected_word = f.readline()
    return selected_word

def get_char_from_user():
    while True:
        ch = input("Enter char: ")
        if len(ch) == 0:
            print("empty guess not allowed")
            continue
        return ch[0]
        break

def play_hangman(path, GUESS_LIMIT):
    word = get_random_line_from_file(path)
    if word == None:
        print("Unable to load word from file")
        return
    word_line = ['__ '] * len(word)
    guesses = 0
    while guesses < len(GUESS_LIMIT):
        char = get_char_from_user()
#stopping here until I get to object-oriented design