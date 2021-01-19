l1 = [0.95, 0.65, 0.7,0.8, 0.55]
try:
    a = int(input("Enter a?"))
    b = int(input("Enter b?"))
    if b == 0:
        raise ArithmeticError
    else:
        print("a/b = ", a/b)

except ArithmeticError:
    print("The value of b can't be 0")


l2 = []
