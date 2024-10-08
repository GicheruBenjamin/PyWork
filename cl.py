
class Language:
    def __init__(self) -> None:
        self.name = "English"
        self.spoken = "English"
        self.official = True
        self.native = True
        self.language = "English"
        
my_lang = Language()
print(f"I know how to speak {my_lang.name}")

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)
        
    def list_employees(self):
        print(f"Department: {self.name}")
        for employee in self.employees:
            print(employee)
    def no_of_employees(self):
        return len(self.employees)
            
my_working_department = Department("IT")
my_working_department.add_employee("John")
my_working_department.add_employee("Jane")
my_working_department.no_of_employees()
my_working_department.list_employees()




class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

    def get_full_address(self):
        return f"{self.street}, {self.city}, {self.zipcode}"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee:
    def __init__(self, name, age, address):
        self.person = Person(name, age)
        self.address = Address(address['street'], address['city'], address['zipcode'])

    def get_employee_info(self):
        return f"Name: {self.person.name}, Age: {self.person.age}, Address: {self.address.get_full_address()}"

# Creating instances and accessing attributes
employee_info = {
    'name': 'John Smith',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'zipcode': '12345'
    }
}

employee = Employee(**employee_info)
print(employee.get_employee_info())



class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

# Creating instances and accessing attributes
rectangle = Rectangle(width=5, height=3)
print("Width:", rectangle.width)
print("Height:", rectangle.height)
print("Area:", rectangle.get_area())
print("Perimeter:", rectangle.get_perimeter())
print("Diagonal:", rectangle.get_diagonal())
    
    
    
class Robot:
    def __init__(self, model):
        self.model = model

    def move(self):
        return "Robot is moving."

class Bird:
    def __init__(self, species):
        self.species = species

    def fly(self):
        return "Bird is flying."

class FlyingRobot(Robot, Bird):
    def __init__(self, model, species):
        Robot.__init__(self, model)
        Bird.__init__(self, species)

    def perform_actions(self):
        return f"Robot is {self.move()}, and it can also {self.fly()}."

# Creating instances and accessing attributes
flying_robot = FlyingRobot(model="XR-5000", species="Falcon")
print("Model:", flying_robot.model)
print("Species:", flying_robot.species)
print("Actions:", flying_robot.perform_actions())    


class Shape:
    def __init__(self, sides):
        self.sides = sides

    def get_sides(self):
        return self.sides

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(4)  # Calling grandparent class constructor
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def is_square(self):
        return self.width == self.height

# Creating instances and accessing attributes
square = Square(side_length=5)
print("Number of sides:", square.get_sides())
print("Area:", square.get_area())
print("Is it a square?:", square.is_square())


class Ops:
    @staticmethod
    def add(arg1, arg2):
        return arg1 + arg2

print(Ops.add(55, 77))


class Boutique:
    bik:int = 0 #Boutiques I know
    def __init__(self, name:str, location: str):
        self.name = name
        self.location = location
        Boutique.bik += 1
    
Favbq: Boutique = Boutique("Lanphil", "Tokyo")
print(Boutique.bik) 
Wifbq: Boutique = Boutique("GD", "paris")
print(Boutique.bik)


from abc import ABC, abstractmethod

class Business(ABC):
    def __init__(self, name:str,location:str):
        self.name = name
        self.location = location

    @abstractmethod
    def showlocation(self):
        pass


class Shop(Business):
    '''This class inherits from Business class
    It ensures that it uses the showlocation method because 
    it is an abstract method'''
    def __init__(self, name:str,location:str):
        super().__init__(name,location)
    def showlocation(self):
        
        return self.location
    
uncles_shop: Shop = Shop("Arkposho","Brasil")
print(uncles_shop.showlocation())

class Employee:
    no_of_employees:int = 0
    def __init__(self,name: str, salary: int, work_type: str):
        self.name = name
        self.salary = salary
        self.work_type = work_type
        Employee.no_of_employees += 1
    @abstractmethod
    def get_info(self):
        pass   
class Developer(Employee):
    def __init__(self, name: str, salary: int, work_type: str):
        super().__init__(name, salary, work_type)
        
    def get_info(self):
        return f'Name: {self.name}, Salary: {self.salary}, Work type: {self.work_type}'
    
class Designer(Employee):
    def __init__(self, name: str, salary: int, work_type: str):
        super().__init__(name, salary, work_type)
        
    def get_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Work type: {self.work_type}"
    
Josh:Developer = Developer("Joshua", 20000, "Developer")
Jane:Designer = Designer("Jane", 15000, "Designer")

print(Josh.get_info())
print(Jane.get_info())
print(Employee.no_of_employees)

class Company:  
    def __init__(self, name:str, location:str):
        self.name = name
        self.location = location
    def giveinfo(self):
        return{"name": self.name, "location":self.location}
    
class TechCo(Company):
    def __init__(self, name:str, location:str):
        super().__init__(name, location)
    def giveinfo(self):
        return super().giveinfo()
        
        
Apple:TechCo = TechCo("Apple", "California")
print(Apple.giveinfo())        
  class SequenceDemo:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, index):
        return self.sequence[index]

    def __iter__(self):
        return iter(self.sequence)

    def __contains__(self, item):
        return item in self.sequence

    def __add__(self, other):
        return SequenceDemo(self.sequence + other.sequence)

    def __mul__(self, other):
        return SequenceDemo(self.sequence * other)

    def __repr__(self):
        return f"SequenceDemo({repr(self.sequence)})"

# Create instances of SequenceDemo
sequence2 = SequenceDemo(["a", "b", "c"])

# Access elements using indexing
print(sequence1[0])  # Output: 1
print(sequence2[1])  # Output: b

# Iterate over elements
for item in sequence1:
    print(item)  # Output: 1 2 3

# Check if an element is in the sequence
print(3 in sequence1)  # Output: True
print("d" in sequence2)  # Output: False

# Concatenate sequences
sequence3 = sequence1 + sequence2
print(sequence3)  # Output: SequenceDemo([1, 2, 3, 'a', 'b', 'c'])

# Repeat a sequence
sequence4 = sequence1 * 2
print(sequence4)  # Output: SequenceDemo([1, 2, 3, 1, 2, 3])
      