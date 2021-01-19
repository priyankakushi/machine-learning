list = [1,2,3,4,5,6]
count=1
for i in list:
    print(i)
    if i == 4:
        count1 = 1
        print("item matched")
        count = count + 1
        count1 = count1 + 1
        break
        print("found at", count, "location")

print("found at", count, "location",count1)


'''str1 = "python"
for i in str1:
    if i == "y":
        break

    print(i)'''

'''i = 0
while i != 10:
    print("%d"%i)
    i=i+2
    continue

    i=i+1
    print(i)'''


'''i = 1
for i in range(1,11):
    #if (i==5) or (i==7) or (i==3):
    if i%2 == 0:        # check for even values
        continue

    print("%d"%i)'''


'''for i in [1,2,3,4,5]:
    if i==3:
        pass

    print (i)'''










