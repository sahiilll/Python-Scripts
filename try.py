#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
maximumsum = 0
T = [[]]
def maxSubsetSum(arr,start,stop):
    if len(arr) == 1:
        return arr[0]
    for i in range(start, stop):
        for j in range(i + 2,stop):
            if T[i][j] != None:
                return T[i][j]
            else:
                k =
                T[i][j] = maxSubsetSum(arr,i,j)


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    global T
    for i
    res = maxSubsetSum(arr, 0, len(arr) - 1)

    fptr.write(str(res) + '\n')

    fptr.close()
