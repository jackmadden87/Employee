"""This file is the Employee class"""


class Employee:
    """This is the main class for employees of a company"""

    company = "IronCrow"
    web_address = ".co.uk"

    def __init__(self, first_name: str, last_name: str, salary: int, dob: str = None) -> None:
        """This is the constructor for initializing employees"""

        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.employee_type = "Employee"
        self.dob = dob

    def __repr__(self) -> str:
        """Returns a developer string"""
        return f'Employee: {self.first_name}, {self.last_name}, {self.email}, {self.salary}, {self.employee_type}, ' + \
               f'{self.dob}'

    def __str__(self) -> str:
        """Returns a user string"""
        return f'Employee:\n' + \
               f'\tFirst name: {self.first_name}\n' + \
               f'\tLast name: {self.last_name}\n' + \
               f'\tEmail: {self.email}\n' + \
               f'\tSalary: {self.salary}\n' + \
               f'\tJob: {self.employee_type}\n' + \
               f"\tDate of birth: {self.dob}\n"

    def fullname(self) -> str:
        """Returns the full name of the Employee"""
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self) -> str:
        """Return the email of the employee"""
        email_extension = f'{self.company}{self.web_address}'
        return f'{self.first_name.lower()}.{self.last_name.lower()}@{email_extension.lower()}'


if __name__ == '__main__':
    """Runs if this is the main file"""

    employees = [
        Employee('Jack', 'Madden', 55000, "05/08/1987"),
        Employee('Kirsty', 'Madden', 45000, "25/04/1988"),
        Employee('Evie', 'Madden', 35000, "29/12/2019"),
        Employee('Lily', 'Madden', 20000),
    ]

    for emp in employees:
        print(emp)
