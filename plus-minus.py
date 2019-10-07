'''
problem--

Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

For example, given the array arr=[1,1,0,-1,-1] there are 5 elements, two positive, two negative and one zero. Their ratios should be printed as
0.400000
0.400000
0.200000

Function Description--
Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.
plusMinus has the following parameter(s):
arr: an array of integers

Input Format--
The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers describing an array of numbers .
arr(arr[0],arr[1],arr[2],...,arr[n-1]).

Constraints--
0<n<=100
-100<=a[i]<=100

Output Format--
You must print the following  lines:
1. A decimal representing of the fraction of positive numbers in the array compared to its size.
2. A decimal representing of the fraction of negative numbers in the array compared to its size.
3. A decimal representing of the fraction of zeros in the array compared to its size.

Sample Input--
6
-4 3 -9 0 4 1 
        
Sample Output--
0.500000
0.333333
0.166667
'''

#code here

#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    p=0
    n=0
    z=0
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            n+=1
        else:
            z+=1
    print(p/len(arr))
    print(n/len(arr))
    print(z/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

