#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    res_a,res_b = 0,0
    for i in range(len(a)):
        if a[i] > b[i]:
            res_a += 1
        elif a[i] < b[i]:
            res_b += 1
    return [res_a,res_b]

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()