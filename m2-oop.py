# %%
# Classes
class ClassName:
    pass
obj = ClassName()

class Employee:
    ID = 200
    salary = 300
    department = "HR"
Steve = Employee()
print("ID =", Steve.ID)
Steve.title = "Manager"
print("Title:", Steve.title)
# %%
# Initializers
class Employee:
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department

Steve = Employee(3400, 2000, "HR")
print("ID :", Steve.ID)
# %%
# Class and Instance Variables
class Player:
    teamName = "Liverpool"
    def __init__(self, name):
        self.name = name

p1 = Player('Mark')
p2 = Player('Steve')
print(p1.name)
print(p1.teamName)
print(p2.name)
print(p2.teamName)
# %%
# Methods
class Employee:
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):
        return (self.salary * 0.2)
    
Steve = Employee(3000, 2000, "HR")

print(Steve.tax())
# %%
