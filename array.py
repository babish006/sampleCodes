# all values should be same type, needs to define type using a typecode
# no fixed size
# offers methods
#

import array as ar

integers = ar.array('i',[1,2,3,-4,5,6])
print(integers)
print(integers.buffer_info())
for i in range(len(integers)):
    print(integers[i])

float = ar.array('f', [1.2,2.3,3.4,4.5])
print(float)
float.reverse()
print(float)
for e in float:
    print(e)

char = ar.array('u',['a','b','c','d'])
print(char)
newChar = ar.array(char.typecode,[c for c in char])
for c in newChar:
    print(c)