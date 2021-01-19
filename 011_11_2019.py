def add(* count):   #lambda function
    sum = 0
    for i in count:
        sum = sum+i
    print(sum)
    return sum


print(add(10,20,30))



#python code to illustrate
# filter() with lambda()
li = [5,7,22,97,54,62,77,23,73,61]
final_list = list(filter(lambda x: (x%2 ==0) , li))

print(final_list)

li1 = ['p','r','i','y','a','n','k','a']
list1 = list(filter(lambda y:(y == 'a') or (y == 'e') or (y == "i") or (y == "o") or (y == "u"), li1))
print(list1)

def filterdata(x):
    if x>5:
        return x
result = filter(filterdata,(1,2,6))
print(list(result))

li = [5,7,22,97,54,62,76,43,50,20]
final_list = list(map(lambda y: y*2, li))
print(final_list)

from functools import reduce
li = [5,8,10,20,50,100]
sum = reduce((lambda x, y: x + y), li)
print(sum)

#integer number
integer = -20
print('Absolute value of -20 is:', abs(integer))

integer = -40.05
print('Absolute value of -20 is:', abs(integer))

k = [1,2,3,4,6,]
print(all(k))

l = [4,2,3,0]
print(any(l))

l1 = [0,False]
print(any(l1))

x = 8
y=10
print(eval("x + y / x "))

test1 = []
print(test1, "is", bool(test1))
test1 = 0.0

print(test1, "is",bool(test1))
test1 = None

m = lambda x: x*2
print(m(7))

m = lambda x:print(x**2)

#call a function
m(5)
m(4)

def add(* count):
    sum = 0
    for i in count:
        sum = sum+i
    print(sum)
    return sum


print(add(10,20,30))

def add(* count):
    sum = 2
    for y in count:
        sum = sum+y
    return sum

print(add(5,10,15,20))

ls = [10,20,30,40,50,70,90]
final_list = list(filter(lambda x: (x%2 ==0) , li))

print(final_list)

l2 = [25,20,60,61,34,21]
final_list = list(filter(lambda y: (y%2 == 0) , l2))

print(final_list)

li2 = ["p", "r", "i", "y", "a", "n", "k", "a"]
list = list(filter(lambda y:(y == "a") or (y == "e") or (y == "i") or (y == "o") or (y == "u"), li2))
print(list)

li = [5,7,22,97,54,62,76,43,50,20]
final_list1 = list(map(lambda y: y*2, li))
print(final_list1)

k = [1,2,3,4,5,6]
print(all(k))

integer = -20                                       
print('Absolute value of -20 is:', abs(integer))


def add(a, b):
    c = a+b
    return c
print(3, 5)
                                                    

