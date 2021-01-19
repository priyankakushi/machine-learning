#l1 = [5, 10, 15, 20, 25, 50]
'''a = []
n = int(input("Enter the size of list"))
for i in range(0,n):
    ab = int(input("Enter the number"))
    a.append(ab)
print(a)'''

'''list1 = [10, 15, 20, 5, 9, 1]
list1.sort()
print(list1)
list1.reverse()
print(list1)
list1.insert(2, 100)
print(list1)
list1.pop()
list1.remove(10)
print(list1)'''

'''list2 = [10, 5, 10, 5, 9, 9, 8, 5]

#set1 = {1, 3, 4, 7, 6, 9, 8}
set2 = list2
set3 = (set(list2))
print(set3)'''

'''list2 = [10, 5, 10, 5, 9, 9, 8, 5]
list3 = []
for i in list2:
    if i not in list3:
        (list3.append(i))
        print(list3)

l1 = {int(x) for x in input("Enter a number").split(" ")}

print(l1)

class A:
    def __init__(self):
        super().__init__()
        self.a = 10
        print("method of a")

    def feature1(self):
        print("feature 1")
        print(self.a)

    def feature2(self):
        print("feature 2")
        print(self.a)


class B:
    def __init__(self):
        super().__init__()
        self.a = 10
        print("method of a")

    def feature3(self):
        print("feature 3")
        print(self.a)

    def feature4(self):
        print("feature 4")
        print(self.a)


class C(B,A):
    def __init__(self):
        super().__init__()
        self.a = 10
        print("method of a")

    def feature5(self):
        print("feature 5")
        print(self.a)

    def feature6(self):
        print("feature 6")
        print(self.a)

obj = C()
obj.feature1()
obj.feature2()
obj.feature3()
obj.feature4()
obj.feature5()
obj.feature6()'''

#same class same method
#but run diff. no of marameter

#method overriding
#diff. class, same method, samem no of parameter
#overriding
'''class Animal:
    def speak(self):
        print("speaking")
class Dog(Animal):
    def speak(self):
        print("barking")
d = Dog()
d.speak()


class Bank:
    def getroi(self):
        return 10
class SBI(Bank):
    def getroi(self):
        return 7
class CICI(Bank):
    def getroi(self):
        return 8

b1 = Bank()
b2 = SBI()
b3 = CICI()

print("Bank Rate of interest:", b1.getroi())
print("SBI Rate of interest:", b2.getroi())
print("CICI Rate of interest:", b3.getroi())'''


def mul(a, b):
    return a*b
def add(a, b):
    return a+b

def add(a, b):
    return a-b

def add(a, b):
    return a/b