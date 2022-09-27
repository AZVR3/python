def my_func(param1='default'):
    """
    THIS IS THE DOCSTRING
    """
    print("My first python function! {}".format(param1))

my_func()

def hello_one():
    print("Hello")

def hello_two():
    return "hello"

result1 = hello_two()
print(result1)
hello_one()

def add_num(num1,num2):
    return num1+num2

result2 = add_num("2","3")
print(result2)
print(type(result2))

result2 = add_num(2,3)
print(result2)
print(type(result2))

def add_num_update(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, I need integers!"

result3 = add_num_update(2,3)
print(result3)
print(type(result3))

result3 = add_num_update("2","3")
print(result3)
print(type(result3))

# Lambda Expression

# Filter
mylist=[1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool,mylist)
print(list(evens))

lambda num: num%2 == 0
evens2 = filter(lambda num: num%2 == 0,mylist)
print(list(evens2))

tweet = "Go Sports! #Sports"
result = tweet.split('#')
print(result)

print('x' in [1,2,3]) #Falses
print('x' in [1,2,3,'x']) #True
