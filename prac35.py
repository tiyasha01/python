#define a class employee class with attributes role,department and salary.This class also has a showdetails()
# method.Create an Engineer class that inherits properties from employee and has attributes:name and age

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showdetails(self):
        print("role=",self.role)
        print("department=",self.dept)
        print("salary=",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","it","50000")


engg1=Engineer("elon musk","40")
engg1.showdetails()