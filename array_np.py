from numpy import *

# Integer Array
intArr = array([1,2,3,4])

print(intArr)
print(intArr.dtype)

# Float Array
flArr = array([1,2.5,3,4])
print('\n',flArr)
print(flArr.dtype)

# Integer to Float Conversion
newFlArr = array(intArr,float)
print('\n',newFlArr)
print(newFlArr.dtype)

# Float to Integer Conversion
newIntArr = array(flArr,int)
print('\n',newIntArr)
print(newIntArr.dtype)


# linspace dynamically creates an array
lins = linspace(0,15,20)
print(lins)

# arange
arArr = arange(1,15,2)
print(arArr)

#logspace
logArr = logspace(1,40,5)
print(logArr)
print('%.2f' %logArr[0])

#Zeroes
zeroArr = zeros(10)
print(zeroArr)

#Ones
onesArr = ones(10)
print(onesArr)
print(onesArr,int)