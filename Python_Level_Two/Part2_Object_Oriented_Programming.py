mylist = [1,2,3]
mylist.append(4)
print(mylist)

# How do we build our own object?
# Everything in python is an object
print(type([1,2,3]))
print(type(()))
print(type(200))
print(type(20.0))

# User defined object
class Sample():
    pass

x = Sample()
print(type(x))

#############################################################################################################################################

class Dog():
    # Class object attribute
    # Will always stay true
    species = "mammal"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog(breed = "Lab",name="Sammy")
otherdog = Dog(breed = "Huskie",name="")

print(mydog.breed)
print(mydog.name)
print(otherdog.breed)

# must be in order
thirddog = Dog("Shiba","Cakie")
print(thirddog.breed)
print(thirddog.name)
print(mydog.species)

#############################################################################################################################################

class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r

myc = Circle(3)
myc.radius = 100
print(myc.radius)
print(myc.area())
myc.set_radius(999)
print(myc.radius)
print(myc.area())

#############################################################################################################################################

# Inheritance
class Animal():

    def __init__(self):
        print("Animal created")

    def  who_am_I(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("Dog created")

    def bark(self):
        print("Woof!")

    def eat(self):
        print("Dog eating")

mya = Animal()
mya.who_am_I()
mya.eat()

mydog = Dog()
mydog.who_am_I()
mydog.eat()
mydog.bark()

# Special methods
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed!")

b = Book("Python","Jose",200)
print(b)
print(len(b))
del b
