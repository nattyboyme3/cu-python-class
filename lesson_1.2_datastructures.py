# # Lists (mutable) # #
# The first data structure we will learn is organized only by the order of the elements.
# - Lists are enclosed in square brackets "[]" and elements are separated by commas.
# - Lists can be extremely long (how much memory does your computer have?) but Python handles all the
#   memory allocation and boring stuff like that when you add/remove items in a list
int_list = [10, 20, 30, 40]

# Both of these make an empty list:
empty_list = list()
another_empty_list = []

# Multiple data types in the same list
# - Cool, but not usually very helpful.
b = [1, True, 'Hi!', 4.3]

# List of lists
# - Lists contain objects, and since lists are objects, lists can contain lists!
nested_list = [['Nested', 'lists'], ['are', 'possible']]

# When you want to get data out of a list, you also use square brackets after the list variable to
# indicate which item you want out of the list.
# - You can extract first element with [0], second with [1], etc.

example_list = ['d', 'c', 'z', 'v']
item = example_list[0]

# However, if you want to get the last element, and you can't be bothered to figure out how many there are
# you can use negative numbers.
# - Extract Nth last element by using [-n], so for the last element, it's [-1]
item2 = example_list[-2]
print(item, item2)

# IndexError
# - Python will throw an error if you try to extract an element that doesn't exist
will_throw_error = example_list[10]

# If you want more than one item from the list, you can use a colon between to get multiple:
# - this gets two items from the list, starting at index 1 (list starts at 0), and going to (but not including) index 3
two_items = example_list[1:3]  # => ['c', 'z']

# You can do all sorts of neat things with lists. Here are some of the basic ones:
# - Add an object to the end of a list by adding .append(object) to the end of the list variable
# - The . operator allows you to access methods that come with types like list
# - Most member methods (like append) change the object that they are called on
# - Some, however, just return data about the list
example_list.append('q')  # adds 'q' to the end of the list
example_list.insert(0, 'h')  # inserts the object 'h' at index 0 (at the beginning)
print(example_list)
example_list.sort()  # Does not return anything, just alters the list
print(example_list)
last_element = example_list.pop()  # pop() gets the last thing off of the list, and removes it from the list
print(f'last: {last_element}, rest of list : {example_list}')

# A useful standalone function that works with many things (including strings and lists) is the len() function
# - it measures the length of things, but not always in the way you think
# - in a list, it measures the number of elements, but only at the top level, like in our nested list example
# - in a string, it measures the number of characters
a_nested_list = [['Nested', 'lists'], ['are', 'possible']]
len(nested_list)  # => 2, not 4
a_string = "i am a 26-character string"
len(a_string)

# Did you know? Strings are lists!
# - if you want just one character of a string, put a number in the brackets - [0] gets the first character.
# - The code below "[11:18]" indicates that we want to characters at index 11 to (but not including) 18.
# - Like in many programming languages, Python strings are 0-indexed, so the first character of a string is at index 0.
string1 = 'Qod erat demonstratum. Veni, vidi, vici'
print(string1[0])  # => 'Q'
print(string1[11:18])  # => 'monstra'

# # Dictionaries # #
# Dictionaries are another way of storing/organizing complex data in Python
# - Dictionaries are enclosed in curly braces "{}" and use colons to separate keys from values
# - Elements (composed of a key : value pair) are separated by commas
# This one has strings as keys and numbers as values
d1 = {'axial_force': 319.2, 'moment': 74, 'shear': 23}

# You can also make a dictionary with strings as keys and lists as values
# - Values can be any object.
d2 = {'Point1': [1.3, 51, 10.6], 'Point2': [7.1, 11, 6.7]}

# If you want just the keys of a dictionary, you can get a list of them
print(d1.keys())
# Same with values.
print(d1.values())

# Nested Dictionaries
# - This dictionary has a dictionary inside it, with a list inside that.
d4 = {'Network Team': {'Director': 'Alan', 'Team Members': ['Jeff', 'Lauren', 'Tim O']},
      'Tech Team': {'Director': 'Stephen', 'Team Members': ['Colin', 'Grant', 'Scott D', 'Rich', 'David', 'Jonathan']}
      }

# Extracting values from dictionaries:
# - Unlike lists, dictionaries don't use the position of an object to get it, but its key
# - The key is the portion to the right of the colon for each element.
# - However, like lists, we use square brackets "[]" with the key inside (as a string!) to get the element.
d = {'Nx': 83, 'Mv': 154, 'Mz': 317}
print(d['Mv'])
# For nested dictionaries, you can do this twice to get at the objects one layer down.
print(d4['Network Team']['Director'])
# If you try to get a key that doesn't exist, Python will get mad:
will_throw_more_error = d4['Admin Team']

# Altering Dictionaries
# - To make changes to a dictionary, you simply assign the dictionary location (using [] and the key) to a new object
d['Nx'] = 44
print(d)
# - If you'd like to store data at a new key, just assign a value to a key that doesn't exist yet
d['Qg'] = 76
print(d)

# The 'in' keyword #
# When used like this, "in" will tell you whether the item on the left is contained by the object on the right.
print(2 in [1, 2, 3])  # True
# This is often useful to tell if a bit of data is in a dictionary
print(154 in d.values())  # => True
print('Nx' in d.keys())  # => True
print('SomeKey' in d.keys())  # => False

# Exercise 1: retrieve the 2nd member of the Tech Team from the nested dictionary.

# Exercise 2: Set 'Dr. White' as the director of the Network Team.
