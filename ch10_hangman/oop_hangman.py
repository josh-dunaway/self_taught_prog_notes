import text_art

class RandomWord:
    def __init__(self, filename):
        with open(filename) as f:
            words_list = []
            for line in f:
                words_list.append(line.rstrip('\r\n'))
            import random
            self.word = random.choice(words_list)
    
    def displayWord(self, guessed_letters):
        word_to_display = ''
        for letter in self.word:
            if letter in guessed_letters:
                word_to_display += ' ' + letter + ' '
            else:
                word_to_display += ' _ '
        print(word_to_display)
        return word_to_display

class Hangman:
    STAGES = len(text_art.list_of_hangman_figures)
    def __init__(self):
        self.hangman = text_art.list_of_hangman_figures[0]
    
    def draw(self, num_incorrect_guesses):
        if num_incorrect_guesses >= 0 and num_incorrect_guesses < self.STAGES:
            self.hangman = text_art.list_of_hangman_figures[num_incorrect_guesses]
            print(self.hangman)

class HangmanGame:
    def __init__(self, filename):
        self._filename = filename
        self._secret_word = RandomWord(self._filename)
        self._hangman = Hangman()
        self.num_incorrect = 0
        self.guessed_letters = []

    def _resetGame(self):
        self._secret_word = RandomWord(self._filename)
        self.num_incorrect=  0
        self.guessed_letters = []

    def play(self):
        
        print(text_art.hangman_title)

        playing = 'y'

        while playing.lower() == 'y':
            self._resetGame()
            print("TEST - word = {}".format(self._secret_word.word))
            while self.num_incorrect < self._hangman.STAGES:               
                if len(self.guessed_letters) == 0:
                    self._hangman.draw(self.num_incorrect)
                    self._secret_word.displayWord(self.guessed_letters)
                
                guessed_letter = input('Please guess a letter: ').lower()

                while guessed_letter.isalpha() is False:
                    guessed_letter = input('Only letters allowed! Enter: ').lower()

                while guessed_letter in self.guessed_letters:
                    print('You have already guessed {}. Pick another: '.format(guessed_letter))
                    guessed_letter = input()
                else:
                    self.guessed_letters.append(guessed_letter)
                    if guessed_letter not in self._secret_word.word:
                        print('\nWRONG!')
                        self.num_incorrect += 1
                    self._hangman.draw(self.num_incorrect)
                
                word_status = self._secret_word.displayWord(self.guessed_letters)
                print('Guessed letters: {}'.format(self.guessed_letters))

                if '_' not in word_status:
                    print(text_art.winner)
                    break
            playing = input('Play again? y/n: ')

game = HangmanGame('random_nouns.txt')
game.play()