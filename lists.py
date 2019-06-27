'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format--
The first line contains an integer,n, denoting the number of commands. 
Each line i of the n subsequent lines contains one of the commands described above.

Constraints--
The elements added to the list must be integers.

Output Format--
For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

#code is here

if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        cmd=input().split()
        if cmd[0]=='insert':
            l.insert(int(cmd[1]),int(cmd[2]))
        if cmd[0]=='print':
            print(l)
        if cmd[0]=='remove':
            l.remove(int(cmd[1]))
        if cmd[0]=='append':
            l.append(int(cmd[1]))
        if cmd[0]=='sort':
            l.sort()
        if cmd[0]=='pop':
            l.pop()
        if cmd[0]=='reverse':
            l.reverse()
