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
# Polymorphism
class Shape:
    def __init__(self):
        self.sides = 0

    def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return (self.width * self.height)
    
class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius

    def getArea(self):
        return (self.radius * self.radius * 3.142)
    
shapes = [Rectangle(6, 10), Circle(7)]
print(str(shapes[0].getArea()))
print(str(shapes[1].getArea()))

# %%
# Duck Typing
class Dog:
    def Speak(self):
        print("Woof")

class Cat:
    def Speak(self):
        print("Meow")

class AnimalSound:
    def Sound(self, animal):
        animal.Speak()

sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)

# %%
# Abstract Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)
    
    def perimeter(self):
        return (4 * self.length)

square = Square(4)
# %%
class Shape:
    sname = "Shape"

    def getName(self):
        return self.sname

class XShape(Shape):
    def __init__(self, name):
        self.xsname = name 
    
    def getName(self):
        return (super().getName() + ", " + self.xsname)

circle = XShape("Circle")
print(circle.getName())
# %%
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def Animal_details(self):
        print(self.name + ", " + self.sound)
    
class Dog(Animal):
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family
    
    def Animal_details(self):
        super().Animal_details()
        print(self.family)

class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def Animal_details(self):
        super().Animal_details()
        print(self.color)

d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()
print("")
s = Sheep("Billy", "Baa Baa", "White")
s.Animal_details()
# %%
# Compsition
class Engine:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def printDetails(self):
        print("Engine Details:", self.capacity)

class Tires:
    def __init__(self, tires=0):
        self.tires = tires
    
    def printDetails(self):
        print("Number of tires:", self.tires)

class Doors:
    def __init__(self, doors=0):
        self.doors = doors
    
    def printDetails(self):
        print("Number of doors:", self.doors)

class Car:
    def __init__(self, eng, tr, dr, color):
        self.eObj = Engine(eng)
        self.tObj = Tires(tr)
        self.dObj = Doors(dr)
        self.color = color

    def printDetails(self):
        self.eObj.printDetails()
        self.tObj.printDetails()
        self.dObj.printDetails()
        print("Car color:", self.color)
    
car = Car(1600, 4, 2, "Grey")
car.printDetails()
# %%
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def printDetails(self):
        print("Model:", self.model)
        print("Color:", self.color)

class SedanEngine:
    def start(self):
        print("Car has started.")
    
    def stop(self):
        print("Car has stopped.")
    
class Sedan(Car):
    def __init__(self, model, color):
        super().__init__(model, color)
        self.engine = SedanEngine()

    def setStart(self):
        self.engine.start()
    
    def setStop(self):
        self.engine.stop()
# %%
class Player:
    def __init__(self, ID, name, teamName):
        self.ID = ID
        self.name = name
        self.teamName = teamName

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def getNumberOfPlayers(self):
        return len(self.players)

class School:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def addTeam(self, team):
        self.teams.append(team)

    def getTotalPlayersInSchool(self):
        length = 0
        for n in self.teams:
            length = length + (n.getNumberOfPlayers())
        return length

p1 = Player(1, "Harris", "Red")
p2 = Player(2, "Carol", "Red")
p3 = Player(1, "Johnny", "Blue")
p4 = Player(2, "Sarah", "Blue")

red_team = Team("Red Team")
red_team.addPlayer(p1)
red_team.addPlayer(p2)

blue_team = Team("Blue Team")
blue_team.addPlayer(p2)
blue_team.addPlayer(p3)

mySchool = School("My School")
mySchool.addTeam(red_team)
mySchool.addTeam(blue_team)

print("Total players in mySchool:", mySchool.getTotalPlayersInSchool())
# %%
