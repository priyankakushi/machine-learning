#Iterators with list
'''names = ["soni", "amit", "priyanka", "rahul"]
it = iter(names)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())'''

'''for i in names:
    print(i)'''

'''names = ["soni", "amit", "priyanka", "rahul"]
it = reversed(names)
print(it.__next__())
print(it.__next__())
print(it.__next__())'''

#left to right iterator
#itrator with tuple
'''names = ("soni", "amit", "priyanka", "rahul")
it = iter(names)
print(it.__next__())
print(it.__next__())'''

#right to left reversed
'''names = ("soni", "amit", "priyanka", "rahul")
it = reversed(names)
print(it.__next__())
print(it.__next__())'''



#itrator with set
'''names = {"soni", "amit", "priyanka", "rahul"}
it = iter(names)
print(it.__next__())
print(it.__next__())'''

#iterator with dictionary
names = {"a":"soni", "b":"amit", "c":"priyanka", "d":"rahul"}
it = iter(names)
print(it.__next__())
print(it.__next__())

names = {"a":"soni", "b":"amit", "c":"priyanka", "d":"rahul"}
it = iter(names.values())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

string = "1234567890"
my_it = iter(string)
#left to right iterator
print(my_it.__next__())
print(my_it.__next__())
print(my_it.__next__())
print(my_it.__next__())

string = "1234567890"
my_it = reversed(string)
#right to left reversed
print(my_it.__next__())
print(my_it.__next__())
print(my_it.__next__())
print(my_it.__next__())

my_list = ["mon", "tue", "wen", "thrus", "fri", "sta"]
it = iter(my_list)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

my_list = ["mon", "tue", "wen", "thrus", "fri", "sta"]
for i in my_list:
    print(i)