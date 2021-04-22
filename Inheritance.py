# Inheritance - Creating Subclasses

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# method resolution order
# it looks for the things in the sub class first, then goes to the parrent class
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # let 'Employee's '__init__()' method handle first, last and pay
        super().__init__(first, last, pay)      # same as Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('->', emp.fullname())

dev_1 = Developer('Rahat', 'Khan', 60000, 'Python')
dev_2 = Developer('Abir', 'Hossain', 35000, 'Java')

print('Developer')
print(dev_1.email)
print(dev_2.email)

print(dev_1.pay,'\n')
dev_1.apply_raise()

print('Raising Pay')
print(dev_1.pay)

print(dev_1.fullname())
print(dev_1.prog_lang,'\n')

print('Manager')

mgr_1 = Manager('Aminul', 'Islam', 65000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print('\n', ' After Remove Employee')

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print('-----------')

# 'isinstance()' tels if an object is an instance of a class
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print('-----------')

# 'issubclass()' tels if a class is a subclass of another

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
