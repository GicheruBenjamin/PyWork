
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