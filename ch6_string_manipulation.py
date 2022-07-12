string = """strings that span
multiple lines must be surrounded
by triple quotes"""

print(string)

author = "William Faulkner"
year_born = "1897"

print("Format replaces curly braces with parameters")
print("{} was born in {}.".format(author, year_born))
print("Useful when forming strings from user input")
def complete_the_sentence():
    n1 = input("Enter a noun:")
    v = input("Enter a verb:")
    adj = input("Enter an adjective:")
    n2 = input("Enter a noun:")

    r = "The {} {} the {} {}".format(n1, v, adj, n2)
    print(r)
print("Try typing 'complete_the_sentence()' in console for an example")

print("Showing the split method.")
string = "Hello! My name is Joshua. I enjoy coding. It is fun!"
split_string = string.split(".")
print(split_string)
print("Can split using multiple delimiters with re.split()")

import re
print(re.split('[!,;.-]', string))
print("not sure why it is splitting an empty string at the end")

print("join lets you add new characters between every character in a string:")
print("+".join("abc"))

words = ["First",
         "Second",
         "Third",
         "etc..."]
print(" ".join(words))

print("Strip method removes leading and trailing white space:")
print("     The    ".strip())

print("Replace method replaces first parameter with second:")
print("All animals are equal.".replace('a', "@"))

print("Returning index of first occurence of string passed to index method:")
print("Raises a ValueError: substring not found exception.")
try:
    print("animals".index("m"))
    print("animals".index("z"))
except:
    print("Not found.")

print("\n'in' keyword returns true if string is in other string:")
print("'Cat' in 'Cat in the hat' = " + str("Cat" in "Cat in the hat."))
print("'Rat' in 'Cat in the hat' = " + str("Rat" in "Cat in the hat."))
print("'Rat' not in 'Cat in the hat' = " + str("Rat" not in "Cat in the hat."))

print("\nAdding quotes inside string = use \\\"quotes\\\"")
print('\'It is easier to wrap string in single quotes and have double "quotes" inside\'')
print('Can use \\n for new lines:\nline1\nline2\nline3')
      
#Slicing
print("\nSlicing returns new iterable from subset of items in another iterable.")
print("Has the form [iterable][[start_index:end_index]]")
print("Start_index is inclusive, end_index is not")
fict = ['Tolstoy',
        'Camus',
        'Orwell',
        'Huxley',
        'Austin']
print('Example\nfict = ')
print(fict)
print('fict[1:3] = ')
print(fict[1:3])  
print("Don't need to inclulde start_index if starting from 0: ")
print('fict[:4] = ')
print(fict[:4])
