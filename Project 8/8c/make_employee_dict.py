# Author: Melanie Huynh
# Date: 5/20/2020
# Description: This program takes a class with private data members for name, ID number,
# salary, and email address, and makes a dictionary of the class information.

class Employee:
    """Represents an employee with four private data members: Employee name, ID number, salary, and email address"""
    def __init__(self, name, ID_number, salary, email_address):
        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address
    def get_name(self):
        return self._name
    def get_ID_number(self):
        return self._ID_number
    def get_salary(self):
        return self._salary
    def get_email_address(self):
        return self._email_address

def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):
    employee_dict = {} # empty dictionary to be mutated by Employee data

    for i in range(0, len(emp_names)): # indexes through the lists
        employee_data = Employee(emp_names[i], emp_ids[i], emp_sals[i], emp_emails[i]) # populates the Employee
        employee_dict[emp_ids[i]] = employee_data # adds employee data to a dictionary
    return employee_dict

# emp_names = ["Jean", "Kat", "Pomona"]
# emp_ids = ["100", "101", "102"]
# emp_sals = [30, 35, 28]
# emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
# result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
# print(result)
