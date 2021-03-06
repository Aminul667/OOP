# classmethods and staticmethods

class Employee:
    num_of_emps = 0     #class variable
    raise_amt = 1.04    #class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    #class method works with class insted of instance.
    #they take class
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)            # 'cls(first,last,pay)' is same as 'Employee(first, last, pay)'

    # regular methods automatically pass the instance as the first argument called self
    # classmethods automatically pass the class as the first argument called cls
    # staticmethods don't pass anything automatically. They act like regular function. We just include them in class because they have logical
    # connection with the class

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Rahat', 'Khan', 60000)
emp_2 = Employee('Aminul', 'Islam', 50000)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

Employee.set_raise_amt(1.05) # same thing as 'Employee.raise_amt = 1.05'

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'MD-Mostofa-30000'
emp_str_2 = 'Ratan-Hossain-30000'
emp_str_3 = 'Tanvir-Abir-35000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2021, 4, 21)

print(Employee.is_workday(my_date))