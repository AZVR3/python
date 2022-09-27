#L: Local - Names assigned in any way within a fuction
#E: EFLs = Name in the local scope of any and all enclosing functions
#G: Global - Names assigned at the top-level of a module file
#B: Built-in - Names preassigned in the built-in names module

x = 25

def my_func():
    x = 50
    return x

print(x)
print(my_func())
my_func()
print(x)

# Local
lambda x: x**2

# Enclosing function locals
name = 'This is a global name!'

def greet1():
    name = "sammy"

    def hello():
        print("Hello " + name)

    hello()

def greet2():
    # name = "sammy"

    def hello():
        print("Hello " + name)

    hello()

greet1()
greet2()
print(name)

x = 50

def func(x):
    print('x is:',x)
    x = 1000
    print('local x changed to:',x)

func(x)
print(x)

def func():
    global x
    x = 1000

print("before function call, x is:",x)
func()
print("after function call, x is:",x)
