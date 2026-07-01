'''
3) Nested IF
If (Condition):
    If (Condition):
        Statement
    Else :
        Statement

'''

a = int(input("Enter A :"))
b = int(input("Enter B :"))
c = int(input("Enter C :"))
if a>b:
    if a>c:
        print("A is a Max Number:")
    else :
        print ("C is Max Number:")
elif b>c:
    print("B is Max Number:")
else:
    print("C is Max Number:")
