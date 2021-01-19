#create a class named MyClass
'''class MyClass:
    #assign the values to the MyClass attributs
    number = 0
    name = "abc"

def Main():
    #Creating an object of the MyClass. Here, "me" is the object
    me = MyClass()

    #Accessing the attributes of MyClass using the dot(.)operator
    me.number = 1337
    me.name

    #str is an build- in function that creates an string

    print(me.name + " " + str(me.number))

if __name__=="__main__":
    Main()



class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

        #object of Laptop class(Inner class)
        #self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll_no)
        #self.lap.display()

    class Laptop:
        def __init__(self):
            self.brand = "sony_Vaio"
            self.cpu = "i5"
            self.ram = "8 GB"

        def display(self,brand,cpu,ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
            print(self.brand, self.cpu, self.ram)

s1 = Student("Akshay", 2)
s2 = Student("Rajat", 10)
print()

s1.show()
s2.show()

lap1 = Student.Laptop()
print()
lap1.display('HP', 'i5', '16 GB')

class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def bark(self):

        print("dog barking")

d = Dog()
d.bark()
d.speak()'''


#create a class named MyClass
class MyClass:
    #assign the values to the MyClass attributs
    number = 0
    name = "abc"

def Main():
    #Creating an object of the MyClass. Here, "me" is the object
    me = MyClass()

    #Accessing the attributes of MyClass using the dot(.)operator
    me.number = 1337
    me.name

    #str is an build- in function that creates an string

    print(me.name + " " + str(me.number))

if __name__=="__main__":
    Main()






