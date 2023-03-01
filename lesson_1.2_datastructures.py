# # Lists (mutable) # #
# List with integers
a = [10, 20, 30, 40]

# Multiple data types in the same list
b = [1, True, 'Hi!', 4.3]

# List of lists
c = [['Nested', 'lists'], ['are', 'possible']]

# Extract first element
example_list = ['d', 'c', 'z', 'v']
item = example_list[0]

# Extract second last element
item2 = example_list[-2]
print(item, item2)

# IndexError
will_throw_error = example_list[10]

# Common List methods
example_list.append('q')
example_list.insert('h')
print(example_list)
example_list.sort()
print(example_list)
last_element = example_list.pop()
print(f'first: {last_element}, rest of list : {example_list}')

# # Dictionaries (mutable)# #
# Strings as keys and numbers as values
d1 = {'axial_force': 319.2, 'moment': 74, 'shear': 23}

# Strings as keys and lists as values
d2 = {'Point1': [1.3, 51, 10.6], 'Point2': [7.1, 11, 6.7]}

# Keys of different types (int and str, don't do this!)
d3 = {1: True, 'hej': 23}

print(d1.keys())
print(d1.values())

# Nested Dictionaries
d4 = {'Network Team': {'Director': 'Alan', 'Team Members': ['Jeff', 'Lauren', 'Tim O']},
      'Tech Team': {'Director': 'Stephen', 'Team Members': ['Colin', 'Grant', 'Scott D', 'Rich', 'David', 'Jonathan']}
      }

# Extracting values from dictionaries:
d = {'N': 83, 'My': 154, 'Mz': 317}
print(d['My'])
print(d4['Network Team']['Director'])

# # The 'in' operator # #
print(2 in [1, 2, 3])


