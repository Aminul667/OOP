class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # check the output without this method first
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # we can customize how addation works for our object by creating '__add__' method
    # we want to calculate total salary by just adding employees together (it can be done different and simple way too) 
    def __add__(self, other):
        return self.pay + other.pay     # self is the left side of the addation and other is the right side of addation

    # another example like addation
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Rahat', 'Khan', 60000)
emp_2 = Employee('Aminul', 'Islam', 55000)


print(emp_1)

# this directly call '__repr__' and '__str__' method
print(repr(emp_1))      # same as emp_1.__repr__()
print(str(emp_1))       # same as emp_1.__str__()

print(emp_1 + emp_2)

print(len(emp_1))

