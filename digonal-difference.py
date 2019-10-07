'''
problem--

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9=15. The right to left diagonal = 3+5+9=17. Their absolute difference is |15-17|=2.

Function description

Complete the digonal difference function in the editor below. It must return an integer representing the absolute diagonal difference.

diagonalDifference takes the following parameter:

arr: an array of integers .
Input Format

The first line contains a single integer, n, the number of rows and columns in the matrix arr.
Each of the next n lines describes a row, arr[i], and consists of  space-separated integers arr[i][j].

Constraints--
-100<=a[i][j]<=100

Output Format--
Print the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input--
3
11 2 4
4 5 6
10 8 -12

Sample Output--
15

Explanation--
The primary diagonal is:
11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:
     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

Note: |x| is the absolute value of x
'''

#code here

#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    d1=0
    d2=0
    for i in range(len(arr)):
        d1+=arr[i][i]
        d2+=arr[i][len(arr)-i-1]
    diff=d1-d2
    if diff<0:
        diff=-diff
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

