# Basics
'Hello'
"Hello"

"I'm a dog"

mystring = 'Hello World'
print(mystring)
print(mystring[0])
print(mystring[-1])
print(mystring[3])

print(mystring[2:])
print(mystring[4:])
print(mystring[:2])
print(mystring[:4])
print(mystring[2:5])
print(mystring[:])
print(mystring[::2])

x = mystring.upper()
print(x)
y = mystring.lower()
print(y)
z = mystring.capitalize()
print(z)
a = mystring.split()
print(a)
b = mystring.split('o')
print(b)

x = "Insert another string here: {}".format("INSERT ME!")
print(x)
y = "Item One: {x} Item Two: {y}".format(x = "dog", y = "cat")
print(y)
z = "Item One: {x} Item Two: {x}".format(x = "dog", y = "cat")
print(z)
