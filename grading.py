'''
problem--

HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
For example,grade=84 will be rounded to 85 but grade=29 will not be rounded because the rounding would result in a number that is less than 40.

Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.

Function Description--
Complete the function gradingStudents in the editor below. It should return an integer array consisting of rounded grades.

gradingStudents has the following parameter(s):

grades: an array of integers representing grades before rounding

Input Format--
The first line contains a single integer, , the number of students.
Each line i of the n subsequent lines contains a single integer, grade[i], denoting student i's grade.

Constraints--
0<=n<=60
0<=grade[i]<=100

Output Format--
For each , print the rounded grade on a new line.

Sample Input 0--
4
73
67
38
33

Sample Output 0--
75
67
40
33

'''

#code here

#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    l=[]
    for i in grades:
        if i>=38:
            d=i//5
            r=i%5
            if r>0 and ((d+1)*5)-i<3:
                i=(d+1)*5
            else:
                i=i
        l.append(i)
    return l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

