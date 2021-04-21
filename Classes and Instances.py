#instance and instance variable
class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    # create method to show full name
    def fullname(self):
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("rahat", "khan", 50000) #creating instance
emp_2 = Employee("abir", "hossain", 40000) #creating instance

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname()) # same as 'Employee.fullname(emp_1)'
print(emp_2.fullname())