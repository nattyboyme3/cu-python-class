# # Hello World # #
# - This is a function call. The function, in this case is the pre-written standard library function "print()"
# - When this function is called, it writes out whatever string was passed into it to the screen.
# - The string we pass into it is called an argument. Functions can have 0 or many arguments.
# - You can even write your own functions. More on all of this later.
print("hello world")

# Simple Data Types
# - Python comes with several simple data types that can hold information.
# - Later on, we will assign these literal values to variables, so that we reference them later and manipulate them.
# - Strings are essentially a list of characters, surrounded by either double ("") or single ('') quotes.
# - Integers and Floats store numbers. Integers don't have any decimal places, while floats do.
type('I am a string')  # str
type(34)  # int
type(23.8075)  # float

# There is also a special Python "None" type
# - An object has a type of "None" when Python can't possibly know what it is, like objects that don't exist yet.
# - When we ask Python for the type of this object, it will return a class of "NoneType".
# - A lot of common python errors come from trying to operate on a "NoneType" variable.
type(None)

# Booleans (note capital letters) indicate a simple 1 or 0, true or false, on or off.
# - In python, these can be converted directly to 0 (False) or 1 (True), but it's often
#   more readable to just leave them as they are.
# - Many functions (including built-in ones like "isinstance()") return a boolean value.
yes = True
no = False
isinstance(10, int)  # => True
isinstance('asdf', int)  # => False

# Of course, these can be combined using the operators "and" and "or"
#  - a boolean phrase joined by "and" evaluates to "True" if (and only if) all the elements evaluate to true
#  - boolean phrases can be grouped by parentheses to join and combine "and" and "or" phrases
#  - if you don't specify groupings for booleans, they will be evaluated left to right
also_no = yes and no
also_yes = yes or no
also_also_yes = no and no and no or yes  # => true  -- implied parentheses: (no and no and no) or yes
also_also_no = no and (no and no or yes)  # => false

# Assigning Variables
# - To assign a variable in python, just give it a name, and set it equal to something.
# - Names can contain letters, numbers, hyphens, or underscores
# - Variable names must start with a letter or an underscore
# - Variables can be assigned in the following ways
#       - Variables can have objects directly assigned (sometimes these are called 'Literals'),
#       - Variables can be assigned the value of an expression (combining objects with operators like '+' or 'and')
#       - Variables can be assigned the result of a function call. Some functions return data, and some don't.
#         Note: if you assign a variable to the result of a function that doesn't return anything,
#         you might get a "NoneType"
a = 1
b = 'this is a string'
c = 3.1415926
d = True
print("A is: ")
print(a)
print("B is: ")
print(b)
print("C is: ")
print(c)
print("D is: ")
print(d)

# # Math Operations # #
# Python, like many programming languages, is good at math. Doing math in Python is like doing it on a chalkboard
# - Simply write out the equation you want to calculate, and Python takes care of the rest.
# - All your usual arithmetic operators work like you'd expect them to.
# - We are storing the answers to all these calculations in variables, and printing them out afterwards.
# - Note that after a division step (even one that works out to even numbers), the type returned is a float.
# - That is, unless we force it to be an int again (see f=, below)
a = 24 + 12 - 10  # 26
b = (4 + a) * 3  # 90
c = b / 10  # 9.0 -> float
d = int(c)  # 9 -> int
print("A is: ")
print(a)
print("B is: ")
print(b)
print("C is: ")
print(c)
print("D is: ")
print(d)

# # String Operations # #
# Much of the data that you will receive will (at least at first) be a string. Strings in python are very flexible.
# - Strings can be surrounded by either single (') or double (") quotes
# - Inside a string, you can use the other kind of quotes without any special gymnastics
# - If you need to use a quote of the same type that surrounds the string, you can escape it with a backslash (\)
# - Other special characters (like line returns) can be escaped the same way.
string1 = 'John Jacob Jingleheimer Schmidt'
string2 = 'his name is "my" name, too'
string2 = "his name is \"my\" name, too"  # Can use either ' or "
string_with_line_returns = 'line 1\nline2'
print(string2)
print(string_with_line_returns)

# String addition
# - Strings can be added together to combine them (called 'concatenation').
# - You can combine literals with variables in these additions
string3 = string1 + ", " + string2

# - Can also multiply strings (but not subtract or divide them)
a_string = 'a'
print(a_string * 3)  # 'aaa'

# - You can use the built-in len() function get the length of string
# - This also works for many other data structures, like lists
print(len(string3))

# # Methods # #
# - The . operator allows you to access methods that come with objects like strings
# - Some member methods change the object that they are called on, but some return data
# - You can access member methods by adding a . after the variable, and adding a method name.
# - PyCharm should suggest method names that exist for objects when you type a dot after the variable name.

# The basic string methods allow you to:
# - test strings for what they start and end with
# - count the number of characters or repeated substrings in a string
# - replace certain characters or substrings with others
print(string3.startswith("schmidt"))  # False
print(string3.endswith("schmidt"))  # True
print(string3.upper())  # Make it SHOUT
print(string3.count('J'))  # 3
print(string3.replace('J', 'X'))  # 'Xohn Xacob Xingleheimer Schmidt, his name is my name, too'
print(string3.swapcase())  # 'jOHN jACOB jINGLEHEIMER SCHMIDT, HIS NAME IS MY NAME, TOO'

# String Formatting - "F-strings"
# - F-strings allow you to format a string, inserting any variable right into the middle of it.
# - there are a lot of format specifiers, which allow you to change how the data (especially numbers) is represented
# - There are lots of ways to achieve this result (string addition, for one), but this is the most concise
a = 2
b = 27
print(f'Multiplication: a * b = {a} * {b} = {a*b}')
print(f'Division: a / b = {a} / {b} = {a/b}')

# f-strings with formatting for number of decimal places
print(f'Division: a / b = {a} / {b} = {a/b:.3f}')   # The part ':.xf' specifies 'x' decimals to be printed
pad_number = 30897
print(f'Padding: {pad_number} padded to 7 digits: {pad_number:0>7}')  # 0>7 pads out to 7 digits with 0's

# You can do most code-like things in the brackets, too!
print(f'Computation inside curly braces: {122**2 / 47}')

verb = "runs"
noun = "llama"
adjective = 'flaps'
# And of course, do mad-lib-style string replacement
print(f'George the {noun} is {adjective}. See how he {verb}.')

# Exercise 1: Create a variable containing your name, and then use f-strings to insert your name into a sentence, like
#   "Hello, my name is George, and I like donuts." Print the string.

# Exercise 2: Use python to calculate your approximate age in weeks. (feel free to assume every year has 365.25 days)
#   Print the result out with a reasonable number of decimal places.
