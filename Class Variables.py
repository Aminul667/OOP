# class variable

class Employee():
    #creating class variable
    num_of_emps = 0
    raise_amount = 1.04

    # '__init__()' method runs automatically whenever a instance is created
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1 #accessing class variable with class name or instance name

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #accessing class variable with instance

emp_1 = Employee('Rahat', 'Khan', 60000)
emp_2 = Employee('Aminul', 'Islam', 50000)

emp_1.raise_amount = 1.05

# 'Employee.raise_amount' and 'emp_1.raise_amount' both are different
print(Employee.num_of_emps)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.__dict__)

print(Employee.__dict__)

Employee.raise_amount = 1.06

print(Employee.num_of_emps)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.__dict__)

print(Employee.__dict__)