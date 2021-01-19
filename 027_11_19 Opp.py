'''class Students:
    def __init__(self,name, roll_no):
        self.name = name
        self.roll_no = roll_no
        #self.marks = marks

    def avg(self,m1,m2,m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3
        self.average = (m1+m2+m3)/3
        print(self.name, self.roll_no, self.average)

stu1 = Students("richa", 2)
stu2 = Students("soni", 5)

stu1.avg(20,30,40)
stu2.avg(30,40,50)'''

#constructor - non parameterized
'''class Student:
    def __init__(self):
        print("This is non parametrized constructor")
    def show(self,name):
            print("Hello",name)

Student = Student()
Student.show("priyanka")'''



'''class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display (self):
        print("ID: %d \n Name: %s"%(self.id,self.name))

emp1 =  Employee("John", 101)
emp2 = Employee("David",200)

emp1.display()
emp2.display()




class Student:
    def __init__(self,name, id, age):
        self.name = name
        self.id = id
        self.age = age
 #create the object of the class student
s = Student("john", 101, 22)

#prints the attribute name of the object s
print(getattr(s, "name"))

#reset the value of attribute age to 23
setattr(s, "age", 30)

#prints the modified value of age
print(getattr(s, "age"))

#prints true if the student contains the attribute with name id
print(hasattr(s, "id"))

#deletes the attribute age
delattr(s, "age")

#this will give an error since the attribute age has been deleted
print(hasattr(s, "age"))


class Employee:
    "commn base class for all employees"
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        #Employee.emCount += 1

    def displayEmployee(self):
        print("Name : %s salary: %d"%(self.name, self.salary))

emp1 = Employee("Akshay", 800000000)
emp1.displayEmployee()


print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)




class Student:
    count = 0
    def __init__(self):
        Student.count = Student.count + 1

s1 = Student()
s2 = Student()
s3 = Student()

print("The number of students:", Student.count)



class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def average(self, mark1, mark2, mark3, mark4, mark5):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.mark4 = mark4
        self.mark5 = mark5
        self.average = (mark1 + mark2 + mark3 + mark4 + mark5)/5
        print(self.name, self.roll_no, self.average)

stu1 = Student("somya", 4)
stu2 = Student("radha", 5)

stu1.average(20, 30, 20, 40, 60)
stu2.average(70, 50, 30, 90, 80)



class School:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def multi(self, no1, no2, no3):
        self.no1 = no1
        self.no2 = no2
        self.no3 = no3
        self.multi = (no1 * no2 * no3)
        print(self.name, self.roll_no, self.multi)

stu1 = School("sudha", 2)
stu2 = School("ritu", 1)

stu1.multi(2, 3, 4)
stu2.multi(1, 2,4)



class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self, mark1, mark2):

        self.mark1 = mark1
        self.mark2 = mark2
        self.sub = (mark1 - mark2)
        print(self.name, self.roll_no, self.sub)

stu1 = Student("rani", 1)
stu2 = Student("ruhi", 2)

stu1.display(10, 4)
stu2.display(20, 5)


class School:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.add = (m1 + m2 + m3)
        print(self.name, self.id, self.add)

obj1 = School("aditi", 120)
obj2 = School("aradhya", 202)

obj1.display(10, 30, 5)
obj2.display(10, 50, 2)


#constructor - non parameterized

class Student:
    def __init__(self):
        print("This is non parametrized constructor")

    def show(self, name):
            print("Hello", name)

Student = Student()
Student.show("priyanka")



class School:
    def __init__(self):
        print("this is student")

    def show(self, name):
        print("Hello", name)

stu = School()
stu.show("arti")


class Student():
    def __init__(self):
        print("This is python")

    def show(self, name):
        print("hi", name)

obj = Student()
obj2 = Student()
obj.show("divya")
obj2.show("ruhi")


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def average(self, m1, m2, m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3
        self.average = (m1 + m2 + m3)/2
        print(self.name, self.roll_no, self.average)

obj1 = Student("riya", 3)
obj2 = Student("richa", 7)

obj1.average(10, 20, 10)
obj2.average(20, 10, 40)



class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def multiply(self, m1, m2,):
        self.marks = m1
        self.marks = m2

        self.multiply = (m1 * m2)
        print(self.name, self.roll_no, self.multiply)
obj = Student("Ansu", 4)
obj2 = Student("radha", 8)
obj3 = Student("aradhaya", 1)

obj.multiply(5, 4)
obj2.multiply(2, 6)
obj3.multiply(3, 7)


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def substraction(self, m1, m2):
        self.marks1 = m1
        self.marks2 = m2
        self.substraction = (m1 - m2)
        print(self.name, self.roll_no, self.substraction)

obj1 = Student("damini", 4)
obj2 = Student("ronit", 3)

obj1.substraction(50, 20)
obj2.substraction(80,10)





class Calculator:
    def __init__(self):
        print("sadfia4")
    def multiply(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.multiply = (num1 * num2)
        return self.multiply
obj1 = Calculator()
print("print return", obj1.multiply(7,8))




a = [1,2,5,6,67,65,43,36,54,6,53,34,67,75,76,45,97,32,22]

def findMaxNumber(a):
    b = 0
    for c in range(a):
        if b < c:
            b = c
            return b


print("number", findMaxNumber(a))


#print("max number", max(a))'''


#constructor - non parameterized
class Student:
    def __init__(self):
        print("This is non parametrized constructor")
    def show(self,name):
            print("Hello",name)

Student = Student()
Student.show("priyanka")

class School:
    def __init__(self):
        print("this is constractor")

    def show(self, name,):
        print("hi", name)

obj = School()
obj.show("soni")




class Student:
    def __init__(self,name, id, age):
        self.name = name
        self.id = id
        self.age = age
 #create the object of the class student
s = Student("john", 101, 22)

#prints the attribute name of the object s
print(getattr(s, "name"))

#reset the value of attribute age to 23
setattr(s, "age", 30)

#prints the modified value of age
print(getattr(s, "age"))

#prints true if the student contains the attribute with name id
print(hasattr(s, "id"))

#deletes the attribute age
delattr(s, "age")

#this will give an error since the attribute age has been deleted
print(hasattr(s, "age"))


class School:
    def __init__(self, name, roll_no, age):
        self.name = name
        self.roll_no = roll_no
        self.age = age

s = Student("soni", 3, 20)
print(getattr(s, "name"))
print()
