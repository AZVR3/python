# Comparison Operators
1 > 2
1 < 2
1 >= 1
1 <= 4
1 == 1
1 == "1"
'hi' == 'bye'
1 != 2

# Logical Operators
(1 > 2) and (2 < 3)
(1 > 2) or (2 < 3)
(1 == 2) or (2 == 3) or (4 == 4)

# Indentation
if 1 < 2:
    print('First Block!')
    if 2 < 3:
        print('Second Block!')

if 1 < 2:
    print('First Block!')
    if 20 < 3:
        print('Second Block!')

if 1 < 2:
    print('Hello')
else:
    print('last')

if 4 < 2:
    print('Hello')
else:
    print('last')

if 1 > 2:
    print('Hello')
elif 3 == 3:
    print('elif ran')
else:
    print('last')

if 1 == 1:
    if 1 > 2:
        print('Hello')
    elif 3 == 3:
        print('elif ran')
    else:
        print('last')

# For loops
seq = [1,2,3,4,5,6]

for item in seq:
    print(item)
    print('hello')

d = {'Sam':1,'Frank':2,'Dan':3}

for item in d:
    print(item)
    print(d[item])

# Iterating Tuples
mypairs = [(1,2),(3,4,),(5,6)]

for item in mypairs:
    print(item)

for (tup1,tup2) in mypairs:
    print(tup1)
    print(tup2)

# While loops
i = 1

while i < 5:
    print('i is: {}'.format(i))
    i = i + 1

# Range function
[1,2,3,4,5]
range(5)
# -> range(0,5)
list(range(0,5))
# -> [0,1,2,3,4]
list(range(0,20,2))
# -> [0,2,4,6,8,10,12,14,16,18]
list(range(0,21,2))
# -> [0,2,4,6,8,10,12,14,16,18,21]

for item in range(10):
    print(item)

# List Comprehension
x = [1,2,3,4]
out = []

for num in x:
    out.append(num**2)

print(out)

out = [num**2 for num in x]
print(out)
