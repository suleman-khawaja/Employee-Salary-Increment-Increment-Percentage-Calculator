class Employee2:
    salary=None
    increment=None
    def salaryprevious(self):
        self.salary=int(input("Give The current salary of your employee(in Rs):  "))
    def salaryincrement(self):
        self.increment=int(input("Give the salary increment you want to provide to your employee:  "))
    @property
    def salafterinc(self):
        return (self.salary + (self.salary * (self.increment)/100))
    @salafterinc.setter 
    def salafterinc(self,salary1):
        self.increment=((salary1 - self.salary)/self.salary)*100
    
e=Employee2()
e.salaryprevious()
e.salaryincrement()
print(f"The salary after increment is {e.salafterinc} Rs")
e.salafterinc=int(input("Give the salary of which you want to calculate the increment:  "))
print(f"The increment is {e.increment}%") 
input("\nProgram ended to Exit Press Enter...")