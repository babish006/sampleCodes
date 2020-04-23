num = int(input('Please enter the number: '))

for j in range(2,num):
    if num % j == 0:
        print(num,'is not a Prime Number.')
        break
else:
    print(num,'is a Prime Number.')

