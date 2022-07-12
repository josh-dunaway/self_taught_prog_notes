# 1 - create list of favorite musicians
favorite_musicians = ["Sigur Ros",
                      "Boogie T",
                      "Ganja White Night",
                      "Iron & Wine",
                      "The Shins",
                      "The XX"]

# 2 - create list of tuples, with each tuple containing long/lat
# of somehwere you've lived or visited
coordinates = [(32.8706371351783, -96.78693135670242),
               (52.54359087082321, 13.374662218727657),
               (-30.134928252272896, -51.22384384965936),
               (28.060640748517663, -16.725272438630817)]

#3 - create dictionary that contains attributes about me:
# height, favorite color, favorite author, etc
about_me = {"height": "167 cm",
            "fav_color": "purple",
            "fav_author": "Tolkien",
            "languages": ["English", "Portuguese", "Spanish"],
            "programming_languages": ["Java", "Python", "C++"]}

# 4 - write program that lets the user ask my height, favorite color,
# or favorite author, and returns the result from dictionary I created
def print_numbered_list(lst = None):
    if lst == None:
        print("No list provided.")
    else:
        index = 0
        for i in lst:
            print(str(index + 1) + ". " + i)
            index += 1

def get_selection_from_user():
    while True:
        try:
            selection = input("enter selection:")
            selection = int(selection) - 1
            if selection >= 0 and selection < len(about_me.keys()):
                return selection
            else:
                print("invalid selection")
        except ValueError:
            print("Invalid Input.")

def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range")

def print_nth_key(dictionary, n=0):
    print(dictionary[get_nth_key(dictionary, selection)])
          
print_numbered_list(about_me.keys())
selection = get_selection_from_user()
print_nth_key(about_me, selection)

# 5 - create dictionary mapping fav. musicians to list of fav. songs by them
library = {"$uicideboy$": ["Mount Sinai",
                             "My Flaws Burns Thr...",
                             "Runnin' Thru the 7th W..."],
             "21 Savage": ["a lot",
                           "monster"],
             "6LACK": ["Free",
                       "Pretty Little Fears",
                       "Seasons",
                       "Switch - DEVAULT Remix"],
             "Ariana Grande": ["7 rings",
                               "boyfriend",
                               "breathin'",
                               "Stuck with U"]}

# 6 - Research Python sets. When would I use a set?
# Sets are unordered, unchangeable, and do not allow duplicates.
# Used to store multiple items ina  single variable
# can contain different data types
set1 = {"abc", 34, True, 40, "male"}
# another way to construct a set
set2 = set(("apple", "banana", "cherry"))
