'''
Task--
You are given a string S. 
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format--
A single line containing a string S.

Constraints--
0<=len(s)<=1000

Output Format--
In the first line, print True if S has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if S has any alphabetical characters. Otherwise, print False. 
In the third line, print True if S has any digits. Otherwise, print False. 
In the fourth line, print True if S has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

Sample Input

qA2

Sample Output

True
True
True
True
True
'''

#code is here

if __name__ == '__main__':
    s = input()
    for i in s:
        if ord(i)>=ord('0') and ord(i)<=ord('9'):
            print("True")
            break
        elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
            print("True")
            break
        elif ord(i)>=ord('a') and ord(i)<=ord('z'):
            print("True")
            break
    else:
        print("False")
        
    for i in s:
        if ord(i)>=ord('A') and ord(i)<=ord('Z'):
            print("True")
            break
        elif ord(i)>=ord('a') and ord(i)<=ord('z'):
            print("True")
            break
    else:
        print("False")

    for i in s:
        if ord(i)>=ord('0') and ord(i)<=ord('9'):
            print("True")
            break
    else:
        print("False")

    for i in s:
        if ord(i)>=ord('a') and ord(i)<=ord('z'):
            print("True")
            break
    else:
        print("False")
    
    for i in s:
        if ord(i)>=ord('A') and ord(i)<=ord('Z'):
            print("True")
            break
    else:
        print("False")

