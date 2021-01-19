# Single Level Inheritance

'''class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def bark(self):

        print("dog barking")

d = Dog()
d.bark()
d.speak()

# Multi Level Inheritance

class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def bark(self):

        print("dog barking")

class cat(Dog):
    def black(self):
        print("dog black")

d = cat()
d.bark()
d.speak()
d.black()

class Animal:
    def speak(self):
        print("Animal speaking")



class A:
    def Adata(self):
        print("Method of A")

class B(A):
    def Bdata(self):
        print("Method of B")

ob = B()
ob.Bdata()
ob.Adata()'''


'''class A:
    def Adata(self):
        print("Method of A")

class B(A):
    def Bdata(self):
        print("Method of B")

obj = B()
obj.Bdata()
obj.Adata()'''


'''class A:
    def Adata(self):
        print("Method of A")

class B(A):
    def Bdata(self):
        print("Method of B")

ob = B()
ob.Bdata()
ob.Adata()'''


'''class A:
    def Adata(self):
        print("Method of A")

class B(A):
    def Bdata(self):
        print("Method of B")

obj = B()
obj.Bdata()
obj.Adata()


class Student:
    def Studentdata(self):
        print("method of student")

class School(Student):
    def Schooldata(self):
        print("method of school")

obj1 = School()
obj1.Schooldata()
obj1.Studentdata()

class X:
    def Xdata(self):
        print("method of x")

class Y(X):
    def Ydata(self):
        print("method of Y")

obj2 = Y()
obj2.Ydata()
obj2.Xdata()


class Amit:
    def Amit(self):
        print("method of Amit")

class Sahu(Amit):
    def Sahu(self):
        print("method of Sahu")

obj = Sahu()
obj.Sahu()
obj.Amit()


#multiple inheritence
class A:
    def Adata(self):
        print("method of A")

class B(A):
    def Bdata(self):
        print("method of B")

class C(B):
    def Cdata(self):
        print("method of C")

obj = C()
obj.Cdata()
obj.Bdata()
obj.Adata()


class Aditi:
    def Aditidata(self):
        print("school of Aditi")

class Bipasha(Aditi):
    def Bipashadata(self):
        print("school of Bipasha")

class Chinkidata(Bipasha):
    def Chinkidata(self):
        print("school of Chinki")

obj = Chinkidata()
obj.Chinkidata()
obj.Bipashadata()
obj.Aditidata()'''


class Animal:
    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def bark(self):
        print("dog barking")

obj = Dog()
obj.bark()
obj.speak()


#multiple level inheritence
class Animal:
    def speak(self):
        print("animal speaking")

class Dog(Animal):
    def bark(self):
        print("dog barking")

class Cat(Dog):
    def cry(self):
        print("cat crying")

obj = Cat()
obj.cry()
obj.bark()
obj.speak()


class A:
    def Adata(self):
        print("method of A")

class B(A):
    def Bdata(self):
        print("method of B")

class C(B):
    def Cdata(self):
        print("method of C")

obj = C()
obj.Cdata()
obj.Bdata()
obj.Adata()


class A:
    def Adata(self,A):
        return A
class B(A):
    def Bdata(self,B):
        return B

class C(B):
    def Cdata(self,C):
        return C

class D(C):
    def Ddata(self,D):
        return D

obj = D()
print(obj.Ddata(5))
print(obj.Cdata(6))
print(obj.Bdata(7))
print(obj.Adata(9))


class A:
    def Adata(self):
        print("inside class A")

class B(A):
    def Bdata(self):
        print("inside class B")

class C(B):
    def Cdata(self):
        print("inside class C")
class D:
    def Ddata(self):
        print(" I am inside class D")

class E(C,D):
    def Edata(self):
        print("inside class E")

obj1 = E()
obj1.Adata()
obj1.Bdata()
obj1.Ddata()
obj1.Edata()


class A:
    def feature2(self):
        print("Inside feature 2")

class B(A):
    def __init__(self):
        super().__init__()




