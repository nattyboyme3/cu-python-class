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
# - This is the type of a variable that has not been assigned
# - When we ask Python for the type of this variable, it will return a class of "NoneType".
# - A lot of common python errors come from trying to operate on a "NoneType" variable.
var = None
type(var)

# Booleans (note capital letters) indicate a simple 1 or 0, true or false, on or off.
# - In python, these can be converted directly to 0 (False) or 1 (True), but it's often
#   more readable to just leave them as they are.
# - Many functions (including built-in ones like "isinstance()") return a boolean value.
yes = True
no = False
isinstance(10, int) #  => True
isinstance('asdf', int) # => False

# Of course, these can be combined using the operators "and" and "or"
#  - a boolean phrase joined by "and" evaluates to "True" if (and only if) all the elements evaluate to true
#  - boolean phrases can be grouped by parentheses to join and combine "and" and "or" phrases
#  - if you don't specify groupings for booleans, they will be evaluated left to right
also_no = yes and no
also_yes = yes or no
also_also_yes = no and no and no or yes # => true  -- implied parentheses: (no and no and no) or yes
also_also_no = no and (no and no or yes) # => false

# Assigning Variables
# - To assign a variable in python, just give it a name, and set it equal to something.
# - Names can contain letters, numbers, hyphens, or underscores
# - Variable names must start with a letter or an underscore
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
# - A few unusual ones are:
#   - "%" (modulo) which does division, but only shows the remainder (e.g. 12 % 5 is  2)
#   - "**" (exponentiation) raises the first number to the power of the second (e.g. 2**3 is 8)
# - We are storing the answers to all these calculations in variables, and printing them out afterwards.
# - Note that after a division step (even one that works out to even numbers), the type returned is a float.
# - That is, unless we force it to be an int again (see f=, below)
a = 24 + 12 - 10  # 26
b = (4 + a) * 3  # 90
c = b / 10  # 9.0 -> float
d = c // 4  # 2.0 -> float
e = d**d  # 4.0 -> float
f = int(e) # 4 -> int
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
print("F is: ")
print(f)

# # String Operations # #
# Much of the data that you will receive will (at least at first) be a string. Strings in python are very flexible.
# - Strings can be surrounded by either single (') or double (") quotes
# - Inside a string, you can use the other kind of quotes without any special gymnastics
# - If you need to use a quote of the same type that surrounds the string, you can escape it with a backslash (\)
# - Other special characters can be escaped the same way.
# - Backslashes can also be used insert things like line returns (\n) and tab characters (\t)
# - Triple-quoted strings do not end at the end of a line of python code, but continue until the end triple-quote.
string1 = 'john jacob jingleheimer schmidt'
string2 = 'his name is "my" name, too'
string2 = "his name is \"my\" name, too"  # Can use either ' or "
string_with_line_returns = 'line 1\nline2'
string_with_more_line_returns = """Roses are red,
Violets are blue.
Coding is fun,
Python is too."""

# String addition
# - Strings can be added together to concatenate.
# - You can combine literals with variables in these additions
# - strings can be split up into their component parts using square brackets - []
# - The code below "[11:12]" indicates that we want to grab 12 characters, starting with the one at index 11
# - Like in many programming languages, Python strings are 0-indexed, so the first character of a string is at index 0.
string3 = string1 + ", " + string2
print(string3)
print(string1[11:12])

# - Can also multiply strings (but not subtract or divide them)
a_string = 'a'
print(a_string * 3)  # 'aaa'

# - You can use the built-in len() method get the length of string
# - This also works for many other data structures, like lists
print(len(string3))

# Other common string methods allow you to:
# - test strings for what they start and end with
# - count the number of characters or repeated substrings in a string
# - replace certain characters or substrings with others
print(string3.startswith("schmidt"))
print(string3.endswith("schmidt"))  # True
print(string3.count('j'))  # 3
print(string3.replace('j', 'X'))  # 'Xohn Xacob Xingleheimer schmidt, his name is my name, too'

# String Formatting - "f-string"
# - This method of formatting a string can insert any variable that can be converted to a string right into the middle
# - there are a lot of format specifiers, which allow you to change how the data (especially numbers) is represented
# - There are lots of ways to acheive this result (string addition, for one), but this is the most concise
a = 2
b = 27
print(f'Multiplication: a * b = {a} * {b} = {a*b}')
print(f'Division: a / b = {a} / {b} = {a/b}')

# f-strings with formatting for number of decimal places
print(f'Division: a / b = {a} / {b} = {a/b:.3f}')   # The part ':.xf' specifies 'x' decimals to be printed

# You can do most code-like things in the brackets, too!
print(f'Computation inside curly braces: {122**2 / 47}')

verb="runs"
noun="llama"
adjective='sopping'
# And of course, do mad-lib-style string replacement
print(f'George the {noun} is {adjective}. See how he {verb}.')

# Exercise 1: Create a variable containing your name, and then use f-strings to insert your name into a sentence, like
#   "Hello, my name is George, and I like donuts." Print the string.

# Exercise 2: Using the string variable with your name, insert it into a string, repeated 3 times using the *
# operator. Then, add a line return to the string, and print the whole thing again on a new line.
#   Print the resulting 2-line string 3 times with a single print statement.

# Exercise 3: Use python to calculate your approximate age in weeks. (feel free to assume every year has 365.25 days)
#   Print the result out with a reasonable number of decimal places.
