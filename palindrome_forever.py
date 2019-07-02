'''
problem--
input a number and reverse that number. then sum of both number and check this sum is palindrome or not.
if this sum is palindrome then print that palindrome number otherwise repeat the whole process untill you get palindrome number.

sample input-
123
output-
444

sample input-
224
646
'''

def palindrome(n):
  inputnum=n
  rev=0
  while n:
    rev=rev*10+n%10
    n=n//10

  sum=inputnum+rev
  revsum=sum

  r=0
  while sum:
    r=r*10+sum%10
    sum=sum//10

  if r==revsum:
    print(r)
  else:
    palindrome(revsum)

n=int(input())
palindrome(n)
