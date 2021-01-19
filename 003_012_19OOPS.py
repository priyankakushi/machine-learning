# a = 208^115
# print(a)
#
# b = 215&309
# print(b)
#
# c = 511 | 415
# print(c)
#
#
#
#
# class A:
#     count = 1
#     def __init__(self):
#         self.abc = 1000
#         print("Init method of A")
#
#     def feature1(self):
#         print("Inside feature 1")
#         print(self.abc)
#
#     def feature2(self):
#         print("Inside feature")
#         print(self.abc)
#
#
# class C(A):
#     def __init__(self):
#         super().__init__()
#         print("Init method of C")
#
#     def feature5(self):
#         print("Inside feature 5")
#
#     def feature6(self):
#         print("Inside feature 6")
#
# class B(C):
#     def __init__(self):
#         super().__init__()
#         print("Init method of B")
#
#     def feature3(self):
#         print("Inside feature 3")
#
#     def feature4(self):
#         print("Inside feature 4")
#
# obj = B()
# obj.feature1()
# obj.feature2()
# obj.feature3()
# obj.feature4()
# obj.feature5()
# obj.feature6()
#
#
#
# # How constructor behave in multiple inheritance
#
# class A:
#     count = 1
#     def __init__(self):
#         self.abc = 1000
#         print("Init method of A")
#
#     def feature1(self):
#         print("Inside feature 1")
#         print(self.abc)
#
#     def feature2(self):
#         print("Inside feature")
#         print(self.abc)
#
#
# class C(A):
#     def __init__(self):
#         super().__init__()
#         print("Init method of C")
#
#     def feature5(self):
#         print("Inside feature 5")
#
#     def feature6(self):
#         print("Inside feature 6")
#
# class B(C):
#     def __init__(self):
#         super().__init__()
#         print("Init method of B")
#
#     def feature3(self):
#         print("Inside feature 3")
#
#     def feature4(self):
#         print("Inside feature 4")
#
# class D(A,B,C):
#     def __init__(self):
#         super().__init__()
#         print("init of method D")
#
#     def feature7(self):
#         print("inside feature 7")
#
#     def feature(self):
#         print("init of method 8")
#
# obj = D()
'''
class A:
    count = 1
    def __init__(self):
        self.abc = 1000
        print("Init method of A")

    def feature1(self):
        print("Inside feature 1")
        print(self.abc)

    def feature2(self):
        print("Inside feature")
        print(self.abc)


class C:
    def __init__(self):
        super().__init__()
        print("Init method of C")

    def feature5(self):
        print("Inside feature 5")

    def feature6(self):
        print("Inside feature 6")

class B(C,A):
    def __init__(self):
        super().__init__()
        print("Init method of B")

    def feature3(self):
        print("Inside feature 3")

    def feature4(self):

        print("Inside feature 4")
obj = B()
obj.feature5()
obj.feature6()
obj.feature3()
obj.feature4()


class Employee:
    __count = 0             # class variable
    def __init__(self):
        Employee.__count = Employee.__count + 1

    def display(self):
        print("The number of employee", Employee.__count)

emp = Employee()
emp2 = Employee()

try:
    print(emp.__count)

finally:
    emp.display()'''



class SeeMee:
    def youcanseeme(self):
        return "you can see me"

    def __youcannotseeme(self):
        return "you cannot see me"

#outside class
Check = SeeMee()
print(Check.youcanseeme())
#print(Check._youcannotseeme())
print(Check._SeeMee__youcannotseeme())


class Student:
    def __init__(self, name, roll_no):
        self.__name = name
        self.__roll_no = roll_no

    def display(self):
        print("student1 name")


obj = Student("riya", 2)
obj.display()
obj.display()

print(obj._Student__name)
print(obj._Student__roll_no)


