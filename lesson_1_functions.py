# # Functions # #

# Functions let you abstract out your code
#  - pass in and out information
#  - only write a specific routine once

# this one is dumb. It takes fewer characters to do x+y than add_numbers(x,y)
def add_numbers(one: int, two: int) -> int:
    return one + two


# alternates letters from two strings, for as long as they both have letters
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

def no_return(var1, var2):
    var1+=1
    var2+=1


print(type(no_return(4,5)))


# Method calls can
