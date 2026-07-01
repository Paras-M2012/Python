import random

Data=file=open("Data.txt" , "w")
for i in range(10):
    Data.write(str(random.randint(1,100))+",")

Data.close()

Data = open("Data.txt", "r")
Even = open("Even.txt", "w")
Odd = open("Odd.txt" , "w")
Prime = open("Prime.txt", "w")
l = Data.read().split(",")[:-1]
for i in l:
    if int(i)%2==0:
        Even.write(i+",")
    else:
        Odd.write(i+",")
    if int(i)%2!=0:
        for j in range (3,int(int(i)/2)+1,2):
            if int(i)%j==0:
                break
        else:
            Prime.write(i+",")
    '''
    num = int(i)

    if num % 2 == 0:
        Even.write(str(num) + "\n")
    else:
        Odd.write(str(num) + "\n")
    '''
print(l)

Data.close()
Even.close()
Odd.close()
Prime.close()



print("Data File Content")
Data=open("Data.txt","r")
print(Data.read())
Data.close()


print("Even File Content")
Data=open("Even.txt","r")
print(Data.read())
Data.close()


print("Odd File Content")
Data=open("Odd.txt","r")
print(Data.read())
Data.close()


print("Prime File Content")
Data=open("Prime.txt","r")
print(Data.read())
Data.close()



