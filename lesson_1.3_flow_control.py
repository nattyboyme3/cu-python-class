# # Conditionals (note indentation - tab or spaces) # #
# Conditionals allow you to control the flow of your code, choosing to skip some lines, while choosing to execute others
# - The keyword "if" starts a conditional, and it must be followed by an expression that evaluates to
#   either True or False.

# # Indentation # #
# When a line starts with a tab character (or an even number of spaces), python interprets that as a code block
# - A code block starts after a colon - ":"
# - Code blocks control the sphere of influence of things like an if statement that affect multiple lines.
# - Code blocks end when the indentation returns to the former level.
# - Keep your indentation levels consistent, or Python will get mad.

# Simple "if" statement -- only executes if the expression evaluates to True
boolean = True
if boolean:
    print("this should print - 1")

# Branching
# Only one of the below code blocks will be executed
# - To start a branch, begin with 'if'. As before, if the expression following if is True,
#   the code in that block will be executed. However, none of the other branches will be.
# - To end a branch, use 'else'. If no other path is taken, this will be executed.
# - In the middle, you can add 'elif' statements, like if, followed by conditionals.
# - Each of these elif statements will be executed in order. The first one that evaluates to
#   True will be executed, and the rest of them will be skipped.
if not boolean:
    print("this should not print - 2")
elif boolean:
    print("this should print - 3")
else:
    print("this will not print - 4")
# This works, but please don't do this. Make your code readable.
if not not boolean:
    print("this should print - 5")
else:
    print("this should not print - 6")

# You can, of course, combine your boolean expressions with and & or and group them with parentheses
#  Note: we don't HAVE to put an else at the bottom. However, we leave open the possibility that none of these code
#  blocks will be executed (for instance, if george was not curious, and did not have self-control).
george_is_a_monkey = True
george_is_curious = True
george_has_self_control = False
if george_is_curious and george_is_a_monkey:
    print("Curious George!")
elif not george_is_a_monkey and george_has_self_control:
    print("Definitely not Curious George!")

# # Iterating # #
# The core of dealing with lots of data is being able to process things over and over, iterating over a whole set
# - In Python, this is done with the keywords 'for' and 'while'
# - 'while' is followed by a conditional expression, and will continue to execute its code block until that
#   expression returns False.
# - 'for' is followed by two things: a new variable, and a list (technically called an iterable, because it
#   can work with more than just lists).
# - 'for' will run the code block once for each element in the list On each loop through the code block that follows,
#   the new variable provided will hold the value of that element.
# On this first loop, we use an integer to track how many times we have gone through the loop.
index = 0
# Will run until expression evaluates to False
while index < 5:
    print(f"loop # {index}")
    # new operator! This adds the value of the thing on the right to the variable on the left.
    index += 1

# This for loop should run 6 times, once for each string in the list.
# However, inside the for loop code block, we have added some logic, and some new keywords.
# - the variable "animal" will hold each string as its turn comes up
# - 'continue' will stop the current loop, and return to the TOP for the next item in the list.
# - 'break' will stop the loop entirely, and go to the BOTTOM of the loop.
# Try to predict based on this code what will be printed out.
list_of_animals = ['aardvark', 'giraffe', 'chihuahua', 'turtle', 'coffee', 'ladder']
for animal in list_of_animals:
    if animal == 'chihuahua':
        continue
    if animal == 'coffee':
        break
    print(f'The {animal} is a noble beast.')
print('The End.')

# Exercise 1: Create a list of lists, and loop through each element in the inside lists.
#   Hint: You can add a list as a member of another list like this: list1.append([1,2,3])

# Exercise 2: Create a list of 30 integers, and then write a loop to print every 3rd item, and stop after 20 items.
#   Hint: you can use the built-in method range(0,30) to create a list of the first 30 integers.
