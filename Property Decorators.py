# Property Decorators - Getters, Setters, and Deleters

# first part
# class Employee:

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

# emp_1 = Employee('Rahat', 'Khan')

# print('----------------')
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())
# print('----------------')

# # this didn't change the email address
# emp_1.first = 'Aminul'

# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())
# print('----------------')

# we can use property here
# comment out the first part and run the second part

# second part
# class Employee:

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     # property decorator allows to define a method that we can acces like an attribute
#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first, self.last)

#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

# emp_1 = Employee('Rahat', 'Khan')

# emp_1.first = 'Aminul'

# print(emp_1.first)
# print(emp_1.email)      # emp_1.email() is a method but we can access it like an attribute because of property
# print(emp_1.fullname)   # emp_1.fullname() is a method but we can access it like an attribute because of property

# comment out second first and part then run third part

#third part
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # property decorator allows to define a method that we can acces like an attribute
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # setter allows us to set something like an attribute
    @fullname.setter    # as we want to set fullname
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # we can use deleter to delete
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('Rahat', 'Khan')

emp_1.fullname = 'Aminul Islam' # it goes to setter and set it in fullname

print(emp_1.first)
print(emp_1.email)      
print(emp_1.fullname)

del emp_1.fullname      # deleter can be run by 'del' keyword

print('----------------')
print(emp_1.first)
print(emp_1.email)      
print(emp_1.fullname)