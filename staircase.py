'''
problem--

Consider a staircase of size n=4:

   #
  ##
 ###
####
Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
Write a program that prints a staircase of size n.

Function Description--
Complete the staircase function in the editor below. It should print a staircase as described above.

staircase has the following parameter(s):
n: an integer

Input Format--
A single integer, n, denoting the size of the staircase.

Constraints--
0<n<=100
 .
Output Format--
Print a staircase of size  using # symbols and spaces.

Note: The last line must have  spaces in it.

Sample Input--
6 

Sample Output--

     #
    ##
   ###
  ####
 #####
######

Explanation--
The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of n=6.
'''

#code here

#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    for i in range(1,n+1):
        print(' '*(n-i),'#'*i,sep='')
if __name__ == '__main__':
    n = int(input())

    staircase(n)

