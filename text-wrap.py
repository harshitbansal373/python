'''
problem:
You are given a string S and width w. 
Your task is to wrap the string into a paragraph of width w.

Input Format--
The first line contains a string, S. 
The second line contains the width, w.

Constraints--
0<len(s)<1000
0<=w<=len(s)

Output Format--
Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

#code is here

import textwrap

def wrap(string, max_width):
    l=[]
    for i in range(len(string)):
        l.append(string[i:max_width+i])
        string=string[max_width-1:]
    return "\n".join(l)
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
