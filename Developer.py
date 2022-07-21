"""This file is for the Developer class"""


from Employee import Employee


class Developer(Employee):
    """This is the main class for developers of a company"""

    def __init__(self, first_name: str, last_name: str, salary: int, dob: str, develops: list[str] = None) -> None:
        """This is a constructor for initializing Developers"""

        super().__init__(first_name, last_name, salary, dob)

        if develops is None:
            develops = []
        self.develops = develops

        self.employee_type = "Developer"

    def __repr__(self) -> str:
        """Returns a developer string"""
        return f'{super(Developer, self).__repr__()}, {self.develops}'

    def __str__(self) -> str:
        """Returns a user string"""
        return f'{super(Developer, self).__str__()}' + \
               f'\t{self.develops}\n'


if __name__ == '__main__':
    """Runs if this is the main file"""

    employees = [
        Developer('Jack', 'Madden', 55000, '05/08/1987', ['Python', 'Java']),
        Developer('Kirsty', 'Madden', 45000, '25/04/1988', ['Javascript']),
        Developer('Evie', 'Madden', 35000, '29/12/2019', ['C', 'C++']),
        Developer('Lily', 'Madden', 20000, '', []),
    ]

    for emp in employees:
        print(emp)
