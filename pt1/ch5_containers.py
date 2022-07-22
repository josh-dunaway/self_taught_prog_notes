#creating a list
fruit = list()
fruit = []

#simple list and checking if item in list
def fruit_in_basket(fruit):
    basket = ["Apple", "Orange", "Banana", "Mango"]
    return fruit in basket

print(fruit_in_basket("Apple"))
print(fruit_in_basket("Tylenol"))
print(fruit_in_basket(13))
print(fruit_in_basket(None))

#tuples - immutable
my_tuple = tuple()
my_tuple = ()

rndm = ("M. Jackson", 1958, True)

#tuple with only one item still requires comma
rndm2 = ("test",)

print(1958 in rndm)
print(1959 in rndm)

#3 dictionaries
my_dict = dict()
my_dict = {}
fruits = {"Banana": "Yellow", "Grape": "Purple", "Apple": "Red"}

#add value
fruits["Pineapple"] = "Yellow"
#look up key - prints "Yellow"
print(fruits["Pineapple"])

#use in to check if key in dictionary, can't check if value in dict
print("Grape" in fruits)
print("Mango" in fruits)

#delete key-value pair using del
try:
    del fruits["test"]
except KeyError:
    print("caught KeyError")

rhymes = {"1": "fun",
          "2": "poo",
          "3": "free",
          "4": "door",
          "5": "hive"}

n = input("Type a number:")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found.")

#containers in containers
music = []
rap = ["Kanye West",
       "Jay Z",
       "Eminem",
       "Nas"]
rock = ["Bob Dylan",
        "The Beatles",
        "Led Zeppelin"]
djs = ["Zeds Dead",
       "Tiesto"]

music.append(rap)
music.append(rock)
music.append(djs)

print(music)
print(music[0])
print(music[1])
print(music[2])

#append to list inside list
music[0].append("Kendrick Lamar")
print(music[0])

#list of tuples
locations = list()
la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)
locations.append(la)
locations.append(chicago)
print("list of tuples")
print(locations)

#tuple of lists
eights = ["Edgar Allan Poe", "Charles Dickens"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]
authors = (eights, nines)
print("tuple of lists")
print(authors)

#list of dictionary
bdays = {"Hemingway": "7.21.1899",
        "Fitzgerald": "9.24.1896"}
author_bday_list = [bdays]
print("list of dictionary")
print(author_bday_list)

#tuple of dictionary
author_bday_tuple = (bdays,)
print("tuple of dictionary")
print(author_bday_tuple)

#dictionary with 3 keys (1st key has tuple value, 2nd has list, 3rd has dictionary
ny = {"location": (40.7128, 74.0059),
      "celebs": ["W. Allen",
                 "Jay Z",
                 "K. Bacon"],
      "facts": {"state": "NY",
                "country": "America"}
      }

print("dictionary of tuple, list, and dictionary")
print(ny)
