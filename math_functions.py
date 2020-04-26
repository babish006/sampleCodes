# Fibonacci Sequence Calculation
def fib(n):
    a = 0
    b = 1

    if n <= 0:
        print('\nInvalid input!')
        return False

    print('\nFibonacci Sequence: ')

    if n == 1:
        print(a)
    else:
        print(a, ' ', end='')
        print(b, ' ', end='')

        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c,' ', end='')


n = int(input("Number of Elements: "))

#Fibonacci Sequence
fib(n)
