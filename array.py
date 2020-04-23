# all values should be same type, needs to define type using a typecode
# no fixed size
# offers methods
#

import array as ar

# Integer Array
integers = ar.array('i',[1,2,3,-4,5,6])
print(integers)
print(integers.buffer_info())
for i in range(len(integers)):
    print(integers[i])

# Float Array
float = ar.array('f', [1.2,2.3,3.4,4.5])
print(float)
float.reverse()
print(float)
for e in float:
    print(e)

# String Array
char = ar.array('u',['a','b','c','d'])
print(char)
newChar = ar.array(char.typecode,[c for c in char])
for c in newChar:
    print(c)

# Dynamic Array - Values accepeted from the user
length = int(input('Enter the length of Array: '))
userArr = ar.array('i', [])
for i in range(length):
    x = int(input('Enter the array value: '))
    userArr.append(x)
print(userArr)

# Searching values in a Array
k = 0
search_value = int(input('Enter the value to search: '))
for e in userArr:
    if e == search_value:
        print('Value found at position:',k)
        break
    k+=1
else:
    print('Value not found!')