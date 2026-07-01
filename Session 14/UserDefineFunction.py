#Function With No Argument & No Return value.

def printLine():
    print("-"*70)

printLine()
print("Welcome To The User Defined Function Using Python.")
printLine()


#Function With Argument But No Return Value.

def add(a,b):
    print("Addition : ",a+b)

printLine()
x=int(input("Enter Your Value : "))
y=int(input("Enter Your Value : "))
add(x,y)
printLine()

#Function With Argument & Return Value

def sub(a,b):
    print(a-b)

printLine()
x=int(input("Enter Your Value : "))
y=int(input("Enter Your Value : "))
#ans=sub(x,y)
print("Subtraction : ", sub(x,y))
printLine()
