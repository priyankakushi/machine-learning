'''import math
x = 5
print("sqrt of 5 is", math.sqrt(64))

str1 = "bollywood"

str2 = 'ody'

if str2 in str1:
    print("String found")
else:
    print("String not found")

  print(10+20)'''

#try:
    #block of code
#except Exception l:
    #block of code
#else:
    #this code executes if except block is executed

try:
    fh = open("testfile.txt", "w")
    fh.write("This is my test file for exception handling! !")

except IOError:
    print("Error: can\'t find file or read data")
else:

    print("written content in the file successfully")

    fh = open("testfile.txt", "r+")
    print(fh.read())
    fh.close()
    print(fh.closed)

try:
    fileptr = open("file.txt", "w")
    try:
        fileptr.write("Hi I am good")


    finally:
        fileptr.close()
        print("file.closed")
except:
    print("Error")
else:
    print("inside else block")


try:
    age = int(input("Enter the age?"))
    if age<18:
        raise ValueError
    else:
        print("the age is valid")
except ValueError:
    print("The age is not valid")





