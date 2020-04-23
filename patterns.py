
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