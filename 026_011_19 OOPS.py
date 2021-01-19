'''class Employee:

    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display (self):
        print(self.id,self.name)

obj1 = Employee('abc', 100)
obj2 = Employee('xyz', 105)

obj1.display()
obj2.display()'''

'''class Employee:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display (self):
         print(self.name, self.roll_no)

obj1 = Employee("divya", 2)
obj2 = Employee("riya", 3)
obj3 = Employee("soni", 5)

obj1.display()
obj2.display()
obj3.display()

class Students:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display (self):
        print(self.name, self.id)

obj1 = Students("richa",120)
obj2 = Students("rekha", 100)
obj3 = Students("ruhi", 20)

obj1.display()
obj2.display()
obj3.display()



class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def display (self):
        print(self.first_name, self.last_name, self.age)

p1 = Person("priyanka", "sahu", 20)
p2 = Person("dipika", "kumari", 21)

p1.display()
p2.display()

#print(p1.first_name, p1.last_name, p1.age)
#print(p2.first_name, p2.last_name, p2.age)


#inheritance
class A:
    def Adata(self):
        print("Method of A")

class B(A):
    def Bdata(self):
        print("Method of B")

ob = B()
ob.Bdata()
ob.Adata()


class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

Ob1 = Employee("rohan", "kumar", 10000)
Ob2 = Employee("sohan", "kumar", 20000)

print(Ob1.fname, Ob2.fname)
print(Ob1.fname, Ob1.lname, Ob1.salary)


class Students:
    def __init__(self, name, country, state):
        self.name = name
        self.country = country
        self.state = state

    def display(self):
        print(self.name, self.country, self.state)

obj1 = Students("radhika", "India", "Bihar")
obj2 = Students("poonam", "India", "Delhi")

obj1.display()
obj2.display()


class Employee:
    def __init__(self, name, age,):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

obj1 = Employee("lata", 20)
obj2 = Employee("salu", 21)
obj3 = Employee("jyoti", 23)
obj4 = Employee("sahil", 26)
obj5 = Employee("lila", 20)

obj1.display()
obj2.display()
obj3.display()
obj4.display()
obj5.display()



class Students:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(self.name, self.roll_no, self.marks)

obj1 = Students("shikha", 2, 80)
obj2 = Students("ujala", 5, 50)

obj1.display()
obj2.display()

class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display (self):
        print("ID: %d \n Name: %s"%(self.id, self.name))

emp1 =  Employee("John", 101)
emp2 = Employee("David",200)

emp1.display()
emp2.display()



class Emloyee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display (self):
        print("Name: %d \n ID: %s" %(self.name, self.id))

emp1 = Employee("john", 100)
emp2 = Employee("devid", 150)

emp1.display()
emp1.display()'''


class Employee:
    def __init__(self, first_name, last_name, roll_no):
        self.first_name = first_name
        self.last_name = last_name
        self.roll_no = roll_no
    def display(self):
        print(self.first_name, self.last_name, self.roll_no)

emp1 = Employee("soni", "kumari", 2)
emp2 = Employee("rani", "gupta", 5)

emp1.display()
emp2.display()



class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name, self.id)

obj1 = Student("rahul", 120)
obj2 = Student("rohit", 150)
obj3 = Student("radhika", 200)

obj1.display()
obj2.display()
obj3.display()


#inheritance
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
obj.Adata()'''


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
obj.Aditidata()


class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display (self):
        print("ID: %d \n Name: %s"%(self.id, self.name))

emp1 =  Employee("John", 101)
emp2 = Employee("David",200)

emp1.display()
emp2.display()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print("Name: %s \n ID: %d"%(self.name, self.id))

obj1 = Employee("sonalika", 50)
obj2 = Employee("komolika", 90)

obj1.display()
obj2.display()


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name: %s \n Roll_No: %d:"%(self.name, self.roll_no))

obj1 = Student("rohini", 4)
obj2 = Student("radhika", 9)
obj3 = Student("soniya", 3)

obj1.display()
obj2.display()
obj3.display()


class School:
    def __init__(self, fname, lname, roll_no):
        self.fname = fname
        self.lname = lname
        self.roll_no = roll_no

    def display(self):
        print(self.fname, self.lname, self.roll_no)

obj1 = School("rani", "sahu", 10)
obj2 = School("rahul", "kumar", 15)

obj1.display()
obj2.display()





