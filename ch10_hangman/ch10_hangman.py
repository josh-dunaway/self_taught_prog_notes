import print_text_art_methods
import hangman_methods

RANDOM_WORD_FILEPATH = 'random_nouns2.txt'

print(hangman_methods.get_random_line_from_file(RANDOM_WORD_FILEPATH))

print_text_art_methods.print_hangman_stage(5)