
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