# # Conditionals (note indentation - tab or spaces) # #

# Simplest -- only executes if the expression evaluates to True
boolean = True
if boolean:
    print("this should print - 1")

# Branching -- only one of these blocks will be executed
if not boolean:
    print("this should not print - 2")
elif boolean:
    print("this should print - 3")
# Please don't do this.
elif not not boolean:
    print("this should print - 4")
else:
    print("this should not print - 5")

# # Iterating # #
index = 0
# Will run until expression evaluates to False
while index < 5:
    print(f"loop # {index}")
    index += 1

# Iterates over a List (or any other iterable)
list_of_animals = ['aardvark', 'giraffe', 'chihuahua', 'turtle', 'coffee', 'ladder']
dict_of_animals = {}
for animal in list_of_animals:
    if animal == 'chihuahua':
        # This will stop the execution of this pass of the loop
        continue
    if animal == 'coffee':
        # This will stop the loop entirely
        break
    print(f'The {animal} is a noble beast.')
    dict_of_animals[animal] = [1, 2, 3]


print(dict_of_animals)

# Exercise 1: Create a list of lists, and loop through each element in the inside lists.
#   Hint: You can add a list as a member of another list like this: list1.append([1,2,3])

# Exercise 2: Create a list of 30 integers, and then write a loop to print every 3rd item, and stop after 20 items.
#   Hint: you can use the built-in method range(0,30) to create a list of the first 30 integers.

