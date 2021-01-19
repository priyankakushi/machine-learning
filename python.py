a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,45,65,78,39,45,48, 45, 97, 108, 354647, 3453452435, 342534]
#number dyvide by 2 = priyanka, divide by 3 = amit, divide = 2&3 = soni
#1,priyanka, amit, priyanka, 5, soni

def converter(bar):
    limi = []
    for pri in bar:
        if pri%2 == 0 and pri%3 == 0 :
            #print("soni")
            limi.append("soni")
        elif pri%3==0:
            #print("amit")
            limi.append("amit")
        elif pri%2==0:
            #print("priyanka")
            limi.append("priyanka")
        else:
            #print(pri)
            limi.append(pri)
    print(limi)


#kushbo
#obhsuk



converter(a)

a = "priyanka"
print(a)

