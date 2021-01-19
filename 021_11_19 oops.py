l1 = [10,5,2,3,0.2,1.5,100]
count=0
for i in l1:
    count = count+1

print(count)


j = l1[0]
for a in l1:
    if j < a:
        min = j

    else:
        min = a

    j = min
print(min)


j = l1[0]
for a in l1:
    if j > a:
        max = j

    else:
        max = a

    j = max
print(max)

import re
pat1 = "\w+@(\w+\.)+(com|org|net|edu|in)"
rl = re.match(pat1,"abc123@cs.edu.pec.in")
print(rl.group())


pat1 = "\w+@(\w+\.)+(com|org|net|edu|in)"
rl = re.match(pat1,"abc123@cs.edu.pec.in")
rl.group()

ab1 = "\w+"
r2 = re.match(ab1,"abc123@cs.pec.edu.in")

print(r2.group())


# pat4 = "(?P<name>\w+)@(?P<host>(\w\.)+(com|org|net|edu))"
#
# r3 = re.match(pat4, "xyz@cs.iit.edu")
#
# r3.group('name')
#
# r3.group('host')

# split the string according to the type

'''print(re.split("\W+", "This... is a test, short and sweet, of split()."))

print(re.split("\w+", "This... is a test, short and sweet, of split()."))

print(re.split("\S+", "This... is a test, short and sweet, of split()."))

print(re.split("\s+", "This... is a test, short and sweet, of split()."))'''


# Sub use to substitute
print(re.sub("(blue|white|red|yellow)", "black", "blue socks or white tshirt and red shoes yellow"))

print(re.findall("\d+", "12 dpgs, 11 cats, 1 egg"))


def add(a,b,c,):
    return a+b+c

print(add( 10, 15,c = 20))

p1 = re.compile("[\w\.-]+@[\w\.-]+")

print(p1.match("steve@apple.com").group(0))


print(p1.search("Email steve123jobs@a. today.").group(0))


print(p1.findall("Email steve@apple.com and bill@msft.com now  & abc.123@gmail.com."))


p2 = re.compile("[.?!#$&%]+\s+")

print(p2.split("Tired?   Go# to$ bed% Now!! "))







