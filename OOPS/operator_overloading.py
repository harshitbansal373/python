class Employee:
    #constructor
    def __init__(self):
        reg_no=None
        name=None
        salary=None
        
    
    #function for getting user data    
    def getdata(self):
        self.reg_no=int(input("Enter Reg.No:"))
        self.name=input("Enter Name:")
        self.salary=int(input("Enter Salary:"))
    
    #function for displaying user data 
    def display(self):
        print("\nEmployee Details:")
        print("Name:",self.name)
        print("Reg_no:",self.reg_no)
        print("Salary:",self.salary)
    
    # For checking increased/decreased Salary of an Employee
    def __add__(self,e2):
        if isinstance(e2,Employee):
            return self.salary+e2.salary
        else:
            return self.salary+e2
    
    def __sub__(self,e2):
        if isinstance(e2,Employee):
            return self.salary-e2.salary
        else:
            return self.salary-e2
    
    #comparing two students marks :   == , > , <
    def __eq__(self,e2):
        if self.salary == e2.salary:
            return True
        else:
            return False
    def __gt__(self,e2):
        if self.salary> e2.salary:
            return True
        else:
            return False
        
    def __lt__(self,e2):
        if self.salary< e2.salary:
            return True
        else:
            return False
        
# Object Instantiation        
e1=Employee()
e1.getdata()
e2=Employee()
e2.getdata()
print("e1==e2:",e1==e2)
print("e1>e2:",e1>e2)
print("e1<e2:",e1<e2)

print("Increased Salary:",e1+1000)
print("Decreased Salary:",e2-1000)
