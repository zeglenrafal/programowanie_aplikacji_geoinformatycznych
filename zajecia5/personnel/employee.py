class Employee:
    __max_id = 0

    def __init__(self, first_name, last_name, salary):
        Employee.__max_id += 1
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = Employee.__max_id
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Salary: {self.salary} zł")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary: {self.salary}")

    @classmethod
    def get_max_id(cls):
        return cls.__max_id

# V2 - slajd 11
from abc import ABC, abstractmethod

# class Employee(ABC):
#     def __init__(self, first_name, last_name, employee_id, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.employee_id = employee_id
#         self.salary = salary

#     @abstractmethod
#     def display_info(self):
#         pass