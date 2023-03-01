# # Functions # #

# Functions let you abstract out your code
#  - pass in and out information
#  - only write a specific routine once

# this one is dumb. It takes fewer characters to do x+y than add_numbers(x,y)
def add_numbers(one: int, two: int) -> int:
    return one + two


# This function alternates letters from two strings, for as long as they both have letters
# - This makes sense. Who wants to figure/type/paste this out more than once?
def interpolate_strings(string1: str, string2: str):
    return_string = ""
    index = 0
    for i in string1:
        if not len(string2) > index:
            break
        return_string += i + string2[index]
        index += 1
    return return_string


# - Now you just have to call interpolate_strings(x, y) anytime you want this code executed:
print(interpolate_strings('asdfgh', 'iuedyt76'))


# Functions can also return nothing (often called returning "void"). In Python, a function that doesn't have a "return"
# statement, returns a NoneType when it is called
def print_strings(var1, var2):
    print(var1)
    print(var2)


nothing = print(type(print_strings('asdf','jlk;')))
print(nothing)


# In addition to returning None, functions can also return multiple things at the same time.
# - This function adds and subtracts 5 from an integer.
def add_and_subtract5(a: int):
    return a + 5, a - 5


# When we call it, we get two things back:
plus_five, minus_five = add_and_subtract5(20)
print(f'20 plus 5 is {plus_five}, but twenty minus 5 is {minus_five}')


# Function names can be anything you want, as long as you follow some simple rules:
# - must be composed of a-z, 0-9, A-Z, and underscores
# - must start with a letter or underscore
# However, the Python style guide adds:
#   "Function names should be lowercase, with words separated by underscores as necessary to improve readability."
def call_me_ishmael_some_years_ago_never_mind_how_long_precisely_having_little_or_no_money_in_my_purse_and_nothing_particular_to_interest_me_on_shore_i_thought_i_would_sail_about_a_little_and_see_the_watery_part_of_the_world():
    print('really!?')


# "Can" does NOT imply "should".
call_me_ishmael_some_years_ago_never_mind_how_long_precisely_having_little_or_no_money_in_my_purse_and_nothing_particular_to_interest_me_on_shore_i_thought_i_would_sail_about_a_little_and_see_the_watery_part_of_the_world()


# Functions can also do nothing, using the "pass" statement. Useful for adding code that you will some day fill out with
# additional functionality.
def does_nothing():
    # TODO: Add functionality
    pass

# Exercise 1: Create a function to reverse a string passed into it, and return the reversed string
#   Hint: you can loop through each character in the string using 'for i in string_var:'

# Exercise 2: Create a function to call your first function on each word of a sentence.
#   Hint: You can get a list of words in a sentence by calling the .split(' ') method on the string variable
#     like this: string_var.split(' ')