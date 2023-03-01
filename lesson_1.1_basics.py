# # Hello World # #
print("hello world")

# Simple Variable Types
type('I am a string')  # str
type(34)  # int
type(23.8075)  # float

# special Python "None" type
var = None
type(var)

# Booleans (note capital letters)
yes = True
no = False

also_no = yes and no
also_yes = yes or no
also_also_yes = (yes or no) and yes

# Assigning Variables
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

# # Math Operations (immutable) # #
a = 24 + 12 - 10  # 26
b = (4 + a) * 3  # 90
c = b / 10  # 9.0 -> float
d = c // 4  # 2.0 -> float
e = d**d  # 4.0 -> float
print("A is: ")
print(a)
print("B is: ")
print(b)
print("C is: ")
print(c)
print("D is: ")
print(d)
print("E is: ")
print(e)

# # String Operations (mutable) # #
string1 = 'john jacob jingleheimer schmidt'
string2 = 'his name is my name, too'
string2 = "his name is my name, too"  # Can use either ' or "
string_with_line_returns = """Roses are red,
Violets are blue.
Coding is fun,
Python is too."""

# String addition
string3 = string1 + ", " + string2
print(string3)
print(string1[11:12])

# Can also multiply (but not subtract or divide
a_string = 'a'
print(a_string * 3)  # 'aaa'

# Length of string (also works for other data structures)
print(len(string3))

# Common string methods
print(string3.endswith("schmidt"))  # True
print(string3.count('j'))  # 3
print(string3.replace('j', 'X'))  # 'Xohn Xacob Xingleheimer schmidt, his name is my name, too'

# String Formatting - "f-string"
# - can insert any variable that can be converted to a string
a = 2
b = 27
print(f'Multiplication: a * b = {a} * {b} = {a*b}')
print(f'Division: a / b = {a} / {b} = {a/b}')

# f-strings with formatting for number of decimal places
print(f'Division: a / b = {a} / {b} = {a/b:.3f}')   # The part ':.xf' specifies 'x' decimals to be printed

# You can do most code-like things in the brackets
print(f'Computation inside curly braces: {122**2 / 47}')

# Exercise 1: Create a variable containing your name, and then use f-strings to insert your name into a sentence, like
#   "Hello, my name is George, and I like donuts." Print the string.

# Exercise 2: Take a string variable with your name, and insert it into a string, repeated 3 times using the * operator.
#   Print the resulting string 3 times with a single print statement.

