def student(roll=0,name='xyz'):
    '''display stduent information'''
    a=10
    b=20
    c=a+b
    print(c)
    return
student.sub='python'
print('__doc__ :-',student.__doc__)
print('__name__ :-',student.__name__)
print('__qualname__ :-',student.__qualname__)
print('__module__ :-',student.__module__)
print('__defaults__ :-',student.__defaults__)
print('__code__ :-',student.__code__)
#print('__globals__ :-',student.__globals__)
print('__dict__ :-',student.__dict__)
print('__closure__ :-',student.__closure__)
print('__annotations__ :-',student.__annotations__)
print('__kwdefaults__ :-',student.__kwdefaults__)


'''
output--
__doc__ :- display stduent information
__name__ :- student
__qualname__ :- student
__module__ :- __main__
__defaults__ :- (0, 'xyz')
__code__ :- <code object student at 0x7f022c087d20, file "<ipython-input-24-ec9448d3aced>", line 1>
__dict__ :- {'sub': 'python'}
__closure__ :- None
__annotations__ :- {}
__kwdefaults__ :- None
'''
