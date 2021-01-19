'''def fact(n):     #recorsive method    #recorsive method
    if (n <= 0):
        return("Invalid Input")
    elif(n==1):
        return 1
    else :
        return(n * fact (n-1))

a = int(input("Enter the number"))
print(fact(a))'''


#fibonacci series

def fibo(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else :
        return fibo (n-1) + fibo(n-2)

for i in range(0 , 15):
    print(fibo(i))


a = [x*5 for x in range (2,10,2)]
print(a)


def print2(str1):
    print("This is " + str1)
print2("priyanka")

#recorsive method
'''def fact(n):

    if (n <= 0):
        return ("Invalid input")

    elif (n == 1):
        return 1

    else :
        return (n * fact(n-1))
a = int(input("Enter the number : "))
print(fact(a))'''

'''def fact(n):
    if (n <= 0):
        return ("Invalid input")

    elif (n == 1):
        return 1

    else:
        return (n * fact(n-1))

b = int(input("Enter the number : "))
print(fact(b))rhk'''


#Fibo frequncy / fibo number
#0 1 1 2 3 5 8 13

def fibo (n):
    if (n == 0):
        return 0

    elif (n == 1):
        return 1
    else:
        

        return fibo (n-1) + fibo(n-2)

for i in range(0,10):
    print(fibo(i))



#number = int(input("Enter the number : "))








