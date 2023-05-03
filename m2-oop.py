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
# Class Methods
class Player:
    teamName = 'Liverpool'

    def __init__(self, name):
        self.name = name

    @classmethod
    def getTeamName(cls):
        return cls.teamName
print(Player.getTeamName())
# %%
# Static Methods
class MyClass:

    @staticmethod
    def demo():
        print("I am a static method.")
MyClass.demo()
# %%
# Private and Public Modifiers
class Employee:
    def __init__(self, ID):
        self.__ID = ID
Steve = Employee(480)
print(Steve.ID)
# %%
# Encapsulation with Getters and Setters
class User:
    def __init__(self, username=None):
        self.__username = username

    def setUsername(self, x):
        self.__username = x
    
    def getUsername(self):
        return(self.__username)
Steve = User('steve1')
print(Steve.getUsername())
# %%
class User:
    def __init__(self, username=None, password=None):
        self.__username = username
        self.__password = password

    def login(self, username, password):
        if ((self.__username.lower() == username.lower())
                and (self.__password == password)):
            print("Access granted")
        else:
            print("Invalid")
Steve = User("Steve", "123")
Steve.login("steve", "123")


# %%
# Inheritance -- Parent and Child classes
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
    
class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

# %%
# super()
class Vehicle():
    fuelCap = 90

class Car(Vehicle):
    fuelCap = 50

    def display(self):
        print(super().fuelCap)
        print(self.fuelCap)
obj1 = Car()
obj1.display()
# %%
# Hybrid Inheritance
class Engine:
    def setPower(self, power):
        self.power = power

class CombustionEngine(Engine):
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity

class ElectricEngine(Engine):
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Power:", self.power)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

car = HybridEngine()
car.setPower("2000 CC")
car.setChargeCapacity("250 W")
car.setTankCapacity("20 L")
car.printDetails()
# %%

