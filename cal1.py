'''import cal

print(cal.multiply(10,20))

print(cal.add(5, 7))

print(cal.divide(10, 2))

print(cal.odd_even(20))'''

'''
a, b = 10, 20
c, d = -10.5, 0
print(int.__add__(a, b))
print(float.__abs__(c))
print(int.__bool__(d))
print(str.__add__(str(a), str(b)))'''




class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2

        if s1 > s2:
            return True
        else:
            return False

s1 = Student(60, 90)
s2 = Student(70, 80)

#compare two objects
if s1>s2:
     print("\ns1 wins")

else:
    print("\ns2 wins")


#Example of method overloading

class calc:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a , b=None , c = None ,d = None):
        sum = 0
        if a != None and b != None and c != None and d != None:
            sum = a+b+c+d

        elif a != None and b != None and c != None:
            sum = a+b+c

        elif a != None and b != None:
            sum = a+b

        else:
            sum = a

        return sum

s1 = calc(20, 40)
print(s1.sum(50, 60))
print(s1.sum(50, 60,70,30))
print(s1.sum(50, 60,70))
print(s1.sum(100))



