#1 -
print('#1 - print every character in the string "Camus"\n')

for ch in 'Camus':
    print(ch)

#2 -
print('''\n#2 - write program that collects two strings from user, inserts them
    # into the string 'Yesterday I wrote a [response_one]. I sent it to
    # [response_two]!' and prints new string\n''')

def get_two_strings_from_user() -> []:
    try:
        response_one = input('enter first string: ')
        response_two = input('enter second string: ')
    except ValueError:
        print("Invalid Input.")
    return [response_one, response_two]

def insert_responses_into_example_string(str1: str, str2: str):
    return 'Yesterday I wrote a {}. I sent it to {}!'.format(str1, str2) 
        
strings = get_two_strings_from_user()
print(insert_responses_into_example_string(strings[0], strings[1]))

#3 -
print('''\n#3 - use method to make the string "aldous Huxley was born in
1894." grammatically correct by capitalizing the first letter in the
sentence.\n''')

def capitalize_sentence(sentence):
    return sentence.capitalize()

sentence = 'aldous Huxley was borin in 1894.'
print(capitalize_sentence(sentence));

#4 -
print('''\n#4 - take string "Where now? Who now? When now?" and call
a method that returns a list that looks like:
["Where now?", "Who now?", "When now?"].\n''')

def split_string_along_punctuation(string):
    import re
    # neat little trick to split and include delimiter in string
    return re.findall('.*?[.!\?]', string)

def strip_list_of_strings(string_list):
    new_list = []
    for string in string_list:
        new_list.append(string.strip());
    return new_list;

sentence = 'Where now? Who now? When now?'
split_string = split_string_along_punctuation(sentence)
print(strip_list_of_strings(split_string))

#5 -
print('''\n#5 - take list of words and turn into grammatically correct
string. space between words but not between last word and period.\n''')

def join_words(words):
    return " ".join(words);

#ugly... i'm sure there is a better way of doing this
def remove_one_whitespace_before_punctuation(string):
    result = string.replace(' .', '.')
    result = result.replace(' ,', ',')
    result = result.replace(' ?', '?')
    result = result.replace(' !', '!')
    return result

def build_sentence_from_list_of_words(words):    
    return remove_one_whitespace_before_punctuation(join_words(words))

words = ['The',
         'fox',
         'jumped',
         'over',
         'the',
         'fence',
         '.']

print(build_sentence_from_list_of_words(words))

#6 -
print('''\n#6 - replace every instance of "s" in sentence
with a dollar sign.\n''')

sentence = "A screaming comes across the sky."
print(sentence.replace('s', '$'))

#7 -
print('''\n#7 - use method to find first index of character "m" in string\n''')

def find_first_char_in_string(char, string):
    try:
        return string.index(char)
    except ValueError:
        return None

print(find_first_char_in_string('m', 'Hemingway'))

#8 -
print('''\n#8 - find dialogue in favorite book (containing quotes)
and turn it into a string.\n''')

print('''“I'm a what?" gasped Harry.

"A wizard, o' course," said Hagrid, sitting back down on the sofa,
which groaned and sank even lower, "an' a thumpin' good'un I'd say,
once yeh've been trained up a bit. With a mum an' dad like yours,
what else would yeh be?"\n''');

#9 -
print('''\n#9 - create string "three three three" using concat.,
and then again using multiplication.\n''')

def concat_string_n_times(string: str, n: int) -> str:
    if n > 0:
        result = string
        for x in range(n-1):
            result = result + " " + string
        return result
    return None
            

def mult_string_n_times(string: str, n: int) -> str:
    if n > 0:
        result = string + " "
        result = result * (n)
        return result.strip()
    return string

print(concat_string_n_times('four', 4))
print(mult_string_n_times('three', 3))

#10 - 
print('''\n#10 - slice string to only include characters before first comma\n''')

string = 'It was a bright cold day in April, and the clocks were striking thirteen.'

def slice_string_up_to_first_comma(string: str) -> str:
    return string[slice(string.index(','))]
print(slice_string_up_to_first_comma(string))
