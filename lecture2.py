# x = 10
# print(dir(x))


# class student:
#     "Students are"
# print(dir(student))
# print(student.__doc__)
# obj=student
# print(id(student),id(obj))


# obj= student()
# print(id(obj),id(student))


# class student:
#     def __new__(cls):
#         print("from __new__ method")
#         obj = super().__new__(cls)
#         return obj
#     def __init__(self):
#         print("constructor called")
# obj=student()



# class student:
#     def show(self):
#         print("hello")
# obj = student . __new__(student)
# print(id(student))
# print(id(obj))
    
    
    
# class student:
#     def __init__ (self,x,y,z):
#         print(x,y,z)
# obj=student(10,20,30)
# print(id(obj))


# class student:
#     def __init__(self):
#         print('hello')
#     def __init__(self,x):
#         print('hello')
#     def __init__(self,x,y,z):
#         print('hello')
# obj = student()


# methds:
#     instance method (first instance is self)
#     class  method (first parameter is cls of classmethod)
#     staticmethod (without self and cls as a parameter and staticmethod)