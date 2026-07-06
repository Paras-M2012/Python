print("Start Code")


try:
    a=int(input("Enter A : "))
    b=int(input("Enter B : "))
    c=a/b
    print("Division :", c)
    l=[1,25,89,658,87,52,358]
    index=int(input("Enter Index Numner :"))
    print("Data At Index : ",l[index])
except ZeroDivisionError as e:
    print("Exception Caught : ")
except ValueError as e:
    print("Exception Caught : ")
except IndexError as e:
    print("Exception Caught : ")
finally:
    print("Finally Called")
print("End Code")

'''
in that code they have multiple knowledge:
you can find error
you can except and finally close
'''
