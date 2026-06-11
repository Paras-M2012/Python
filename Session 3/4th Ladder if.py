'''
4) Ladder If
If (Condition):
    Statement
    elif (Condition):
        statement
    elif (Condition):
        statement
    elif (Condition):
        statement
    elif (Condition):
        statement
    elif (Condition):
        statement
Else :
    statement

'''

sname = input("Enter Student Name:")
rno = int(input("Enter Roll No of Student:"))
sub1 = int(input("Enter Marks Of Subject 1:"))
sub2 = int(input("Enter Marks Of Subject 2:"))
sub3 = int(input("Enter Marks Of Subject 3:"))

total = sub1 + sub2 + sub3

per = total / 3

print("Student Name : " , sname)
print("Roll No : ", rno)
print("Total Marks : ", total)
print("Percentage : ", per)

if per>=70:
    print("Distinction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass Class")
else :
    print("Fail")
    
