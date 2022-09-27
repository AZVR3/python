mylist = [1,2,3]
mylist = ['stringstuff',1,2,3,4,5,6,7,8,True,'asdf',[1,2,3]]
print(mylist)
print(len(mylist))

mylist = ['a','b','c','d','e']
print(mylist[1])
print(mylist[-1])
print(mylist[1:])
print(mylist[:3])

mylist[0] = 'NEW ITEM'
print(mylist)
mylist.append("NEW ITEM")
print(mylist)

mylist.append(["x",'y','z'])
print(mylist)

mylist.extend(['x','y','z'])
print(mylist)

item = mylist.pop()
print(mylist)
print(item)

item = mylist.pop(0)
print(mylist)
print(item)

mylist.reverse()
print(mylist)

mylist = [4,5,3,3,56,78,8,4,23]
mylist.sort()
print(mylist)

mylist = [1,2,['x','y','z']]
print(mylist[2])
print(mylist[2][1])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][0])
# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)
