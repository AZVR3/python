# print('hello)
# SyntaxError

# GENERAL SYNTAX
#     try:
#        You do your operations here...
#        ...
#     except ExceptionI:
#        If there is ExceptionI, then execute this block.
#     except ExceptionII:
#        If there is ExceptionII, then execute this block.
#        ...
#     else:
#        If there is no exception then execute this block.

# write and read the data
try:
    f = open('test.txt','w')
    f.write("Test write to test text!")
except IOError:
    print("Error: Could not find file or read data!")
else:
    print("Success!")
    f.close()

# only read the data and not write
try:
    f = open('test.txt','r')
    f.write("Test write to test text!")
except:
    print("Error: Could not find file or read data!")
else:
    print("Success!")
    f.close()
print("Hello world!")

# What if we want to still run some lines of code even after try and except?
try:
    f = open('test.txt','r')
    f.write("Test write to test text!")
except:
    print("Error: Could not find file or read data!")
else:
    print("Success!")
    f.close()
finally:
    print("I always work! No matter what.")
