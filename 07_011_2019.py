'''def detail(name, roll_no):
    print("hi", name, "roll no", roll_no )


# name = input("Enter your name:")
# roll_no = int(input("Enter the roll_no:"))
detail(roll_no=10 , name='priyanka')'''

'''def detail(name, class1=12):  #defualt
    print(name, class1)

name = input("Enter the number: " )
#class1 = int(input("Enter your class1: " ))
detail(name)'''


'''def detail(*names):
    list(names)
    print(type(names))
    for i in names:
        print(i)

#names = input("Enter the number: " )
detail("abc", "xyz", "pqr","gfg")'''

'''def cube(y):
    return y*y*y

print(cube(7))

g = lambda x: x*x*x
print(g(7))

s = lambda x,y,z : x+y+z

print(s(7,2,3))'''



'''m = lambda x:print(x**2)

m(5)
m(2)
m(3)'''

'''m = lambda : print("welcome to lambda function")
#call a function
m()

m = lambda a,b:print("sum=",a+b)

#call a function
m(20,10)
m(5,9)
m(6,30)'''

def add_two(a,b):
    return(a+b)

a=int(input("Enter the number"))
b=int(input("Enter the number"))
add_two(a,b)













