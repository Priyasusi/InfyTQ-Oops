'''#OOPR-Exer-3
#Start writing your code here
Write a Python program to implement the class chosen with its attributes. Also,
represent Jack and Jill as objects of the class chosen
initialize their attributes and
display their details
Create a parameterless constructor in which create the attributes with None
Note: Verification is done only for class structure'''
class Employee:
    def __init__(self):
        self.name=None
        self.age=None
        self.salary=None
c1=Employee()
c1.name="Jill"
c1.salary=40000
c1.age=27
print(c1.name,c1.salary,c1.age)
c2=Employee()
c2.name="Jack"
c2.salary=30000
c2.age=24
print(c2.name,c2.salary,c2.age)

                
                                                    
