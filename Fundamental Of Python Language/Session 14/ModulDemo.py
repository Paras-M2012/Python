import udf

while True:

    print("-"*70)
    print("1. OddEven")
    print("2. Max Of Two")
    print("3. Max Of Three")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Exit")
    print("*"*70)

    choice=int(input("Enter Your Choice : "))

    print("*"*70)


    if choice==1:
        a=int(input("Enter Value : "))
        udf.oddeven(a)
    elif choice==2:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        udf.maxoftwo(a,b)
    elif choice==3:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        c=int(input("Enter Value : "))
        udf.maxofthree(a,b,c)
    elif choice==4:
        a=int(input("Enter Value : "))
        udf.fibonacci(a)
    elif choice==5:
        a=int(input("Enter Value : "))
        udf.prime(a)
    elif choice==6:
        print(" Thank You ")
        print("-"*70)
        break
    else:
        print(" Invalid Choice, Please Try Again ")
        print("*"*70)
        
              
               
              

    
    

               
