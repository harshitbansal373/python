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
# Object Instantiation        
e1=Employee()
e1.getdata()
e1.display()
        