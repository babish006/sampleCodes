#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    zer = 0
    neg = 0
    for i in arr:
        if i>0:
            pos += 1
        elif i == 0:
            zer += 1
        else:
            neg += 1

    return (pos, neg, zer)
if __name__ == '__main__':
    n = int(input("Enter number of elements in array: "))

    arr = list(map(int, input("Enter the elements of array: ").rstrip().split()))

    pos, neg, zer = plusMinus(arr)
    print('{0:.6f}'.format(pos/n))
    print('{0:.6f}'.format(neg/n))
    print('{0:.6f}'.format(zer/n))
