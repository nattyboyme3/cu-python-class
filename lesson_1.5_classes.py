# # Classes # #

# Classes in Python could be a whole class (no pun intended) on its own, but basically,
# they are ways of packaging specific kinds of data and methods/functions that go along with that data for ease of use.

# The class below defines an object of type "ChiaPet". The ChiaPet type has a few properties:
# - a boolean variable stores whether it is alive
# - an integer variable stores its age
# - a string variable stores its name

# These properties are set initially for any new ChiaPet when it's created using the special __init__() method.
# __init__ methods start up the object and set up the attributes so everything is present.

class ChiaPet:
    def __init__(self, name: str, age: int):
        self.alive = True
        self.name = name
        self.age = age

    # Another part of a Python class is a member method. These methods can be called on a specific ChiaPet object,
    # altering it's state. The "self" object refers to the ChiaPet object that this method is called from, and it
    # is always the first argument in any class-based (non-static) function.
    def kill(self):
        self.alive = False

    def resurrect(self):
        self.alive = True

    def rename(self, new_name: str):
        self.name = new_name

    # This function returns something. In this case, it's on of the object's properties, but it could be anything.
    def get_name(self) -> str:
        return self.name

    # There are some other special method calls. This one tells the Python interpreter how to show this object when
    # it needs to convert it to text (i.e. print(ChiaPet))
    def __repr__(self):
        if (self.alive):
            return f"My name is {self.name} and I am {self.age} years old."
        else:
            return f"I'm dead. Stop asking me questions."


# Now let's make some ChiaPets:

tom = ChiaPet("Thomas the Tank Chia", 34)

lewis = ChiaPet("Lewis Carroll", 87)

# Whoops, tom died.
tom.kill()
print(f"is tom alive? {tom.alive}")
print(tom)
# no worries. we can bring him back
tom.resurrect()
print(f"how about now? {tom.alive}")

# let's make lewis say his name
print(lewis)
# let's get his name
lewis_name = lewis.get_name()
print(f"Lewis's name is {lewis_name}")

# Time for a new name
lewis.rename("Lewis & Clark")
print(lewis)


# Make your own class, representing your favorite pastry. Add any properties you feel are important,
#  and make sure you cover the __init__() and __repr__() utility methods.
# For any methods that modify properties, make sure to pass in "self" to the objects.
