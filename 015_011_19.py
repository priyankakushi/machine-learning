# File Input Output
# Write in a file

'''file = open("abc.txt", "w+")

file.write("python is great language. \nYeah its great! !\n")
file. write ("How are you. \nYeah its great! ! \n")
file. write ("Hello Priyanka!\n")


file.close()

# Read through file

file = open("abc.txt", "r+")

#print(file.read())
#print(file.readlines())
print(file.readline())
print(file.readable())

file.close()

# Use of Append in File
# Difference between write and append

file = open("abc.txt", "a+")

file.write("How are you!\n")
file.write("What are you doing today!\n")

print(file.tell())


file.close()'''


file = open("abc.txt", "w+")
file.write("hello Soni!\n")
file.write("how are you!\n")

file.close()

#read through file
file = open("abc.txt", "r+")

#print(file.read())
#print(file.readline())
#print(file.readlines())
print(file.readable())
print(file.read(3))

file.close()

#use of append in file

file = open("abc.txt", "a+")
file.write("what are you doing!\n")
print(file.tell())

file.close()











