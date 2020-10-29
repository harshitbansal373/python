def fizz_buzz():
    '''
    A common technical interview question: print all numbers from 1 to n. If a number is
    divisible by 3, print 'fizz'. If a number is divisible by 5, print 'buzz'. If a number
    is divisible by both 3 and 5, print 'fizzbuzz'.
    '''

    for x in range(1,50):
        if x % 3 == 0 and x % 5 ==0:
            print('fizzbuzz')
        elif x % 3 == 0:
            print('fizz') 
        elif x % 5 == 0:
            print('buzz')
        else:
            print(x)