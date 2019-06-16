n=int(input("enter number of rows: "))
for i in range(1,n+1):
  print(' '*(n-i),'*',' '*(2*(i-1)-1),'*' if i!=1 else '',sep='')
for i in range(n-1,0,-1):
  print(' '*(n-i),'*',' '*(2*(i-1)-1),'*' if i!=1 else '',sep='')

'''output

    *
   * *
  *   *
 *     *
*	*
 *     *
  *   *
   * *
    *

'''
