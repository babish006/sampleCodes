
print('\nFirst Pattern:')
for j in range(4):
    for i in range(4):
        print('# ', end='')
    print('')

print('\nSecond Pattern:')
for j in range(4):
    for i in range(j+1):
        print('# ', end='')
    print('')

print('\nThird Pattern:')
for j in range(4):
    for i in range(4-j):
        print('# ', end='')
    print('')


# The staircase function.
def staircase(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end='')

        for k in range(i+1):
            print('#',end='')
        print()

if __name__ == '__main__':
    n = int(input('Enter the size of staircase: '))

    staircase(n)