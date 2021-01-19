#Break and continue function

'''a = 1
while a < 10:
    print(a)
    a = a+1
    if a == 5:
        break

names = ["soni", "amit", "rahul", "priyanka"]
for i in names:
    print(i)

for i in names:
    if i == "rahul":
        continue
        print(i)'''

#break statement
'''for i in range(10):
    if i == 5:
        break
    print(i)

for x in range(1,8):
    print(x)'''


'''for a in range(15):
    if a == 10:
        continue
    print(a)


# while loop
i = 1
while i<10:
    print(i)
    i = i+1

a = 2
while a <=20:
    print(a)
    a = a+2

name = "priyanka"

while True:
    print("enter your name")
    name1 = input()
    if name1 == name:
        break
print("thanku you", name)'''

# for loop
'''for i in range(20):
    print(i)

for i in range(1, 15, 2):
    print(i)

for a in range(10, 1, -1):
    print(a)


number = "9, 22, 234, 678, 989, 201"
for i in range(0,len(number)):
    print(number[i])

number = "9, 22, 234, 678, 989, 201"
for i in range(0,len(number)):
    if number [i] in "0123456789":
        print(number[i])

number = "9, 22, 234, 678, 989, 201"
for i in range(0,len(number)):
    if number [i] in "0123456789":
        print(number[i], end="")

number = "9, 22, 234, 678, 989, 201"
cleanedNumber =" "
for i in range(0,len(number)):
    if number [i] in "0123456789":
        print(number[i], end="")
newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))'''

'''#while loop
var1 = 0
while var1 < 10:
    print(var1)
    var1= var1+1'''


'''names1 = ["soni", "amit", "rahul", "priyanka"]
names2 = " "
while names2 not in names1:
    names2 = input("enter your name")
else:
    print("you are very good")'''


#list
l1 = [1,2,3,4,5]
print(l1)

l2 = [10.5, 50, "reeya", "hello"]
print(l2)

animals = ["cat", "dog", "rat", "elephant"]
print(animals)

print(animals[2])
print(animals[0])
print(animals[0:3])
print(animals[1:])
print(animals[1:4])

print(animals+l1)
print("hello", animals[0])
print(animals[-1])
print(animals[-2])
print(animals[:])
print(len(animals))
print(type(l2))

var3 = [["cat", "dog", "rat", "elephant"],[10.5, 50, "reeya", "hello"]]
print(var3)
print(var3[1][1])
print(var3[0][2])

names = ["apple", "lichi", "banana"]
print(names)
names.append("guava")
print(names)
names.insert(1, "mango")
print(names)
names.remove("lichi")
print(names)

list = [5, 7, -9, 4, 1, 8]
list.sort()
print(list)
list.reverse()
print(list)

