# # Classes # #

# Classes in Python could be a whole class (no pun intended) on its own, but basically,
# they are ways of packaging specific kinds of data and methods that go along with that data for ease of use.

# The class below defines an object of type "ChiaPet". The ChiaPet type has a few properties:
# - a boolean variable stores whether it is alive
# - an integer variable stores its age
# - a string variable stores its name

# These properties are set initially for any new ChiaPet when it's created using the special __init__() method.
# __init__ methods usually start up the object and set up the attributes so everything is present.
# The __init__ method is automatically called when you instantiate a new instance of a class like this:
# my_object = MyClass()

# All member methods of a class can use a special variable called "self". The "self" object refers the object on the
# left side of the . when using a method, or the new object when creating new instance of this class (in __init__()).
# When you call these methods, "self" is inserted automatically.
# If the method do_something(self) is a member method of MyClass, then we could do the following:
# my_object = MyClass()
# my_object.do_something()
# The "self" object inside the method definition would refer to "my_object" when it was called.

class ChiaPet:
    def __init__(self, name: str, age: int):
        self.alive = True
        self.name = name
        self.age = age

    # Another part of a Python class is a member method. These methods can be called on a specific ChiaPet object,
    # altering it's state. The "self" object refers to the ChiaPet object that this method is called from, and it
    # is always the first argument in any class-based (non-static) method.
    def kill(self):
        self.alive = False

    def resurrect(self):
        self.alive = True

    def get_older(self, years: int):
        self.age += years

    def rename(self, new_name: str):
        self.name = new_name

    # This method returns something. In this case, it's one of the object's properties, but it could be anything.
    # You could just as easily get this by using my_chia_pet.name (see below), but it's a convenient example.
    def get_name(self) -> str:
        return self.name

    # There are some other special method calls. This one tells the Python interpreter how to show this object when
    # it needs to convert it to text (i.e. print(ChiaPet))
    def __repr__(self):
        if self.alive:
            return f"My name is {self.name} and I am {self.age} years old."
        else:
            return f"I'm dead. Stop asking me questions."


# Now let's make some ChiaPets:

tom = ChiaPet("Thomas the Tank Chia", 34)

lewis = ChiaPet("Lewis Carroll", 87)

# We can access their data like this:
print(f"Tom's age is {tom.age}")

# They're objects, so we can put them in a list or dictionary:
pet_list = [tom, lewis]

# Whoops, tom died.
tom.kill()
print(f"is tom alive? {tom.alive}")
print(tom)
# no worries. we can bring him back
tom.resurrect()
print(f"how about now? Is tom alive? {tom.alive}")

# Let's make tom say his name
# When we ask python to convert lewis to a string, it uses the __repr__ method to generate the string that the
# print() method needs to do its job. The __repr__ method is used anytime an object needs to be converted to a string.
print(tom)

# Let's age up Tom a bit.
# notice we don't put the "self" argument in this method call, the tom object is inserted automatically as "self",
# because we used "tom" on the left side of the period.
tom.get_older(12)
print(tom)

# Let's get his name
lewis_name = lewis.get_name()
print(f"Lewis's name is {lewis_name}")

# Time for a new name
lewis.rename("Lewis & Clark")
print(lewis)


# Exercise: Make your own class below, representing your favorite pastry. Add any properties you feel are important,
#  and make sure you cover the __init__() and __repr__() utility methods.
#  For any methods that modify properties, make sure to pass in "self" to the objects.
