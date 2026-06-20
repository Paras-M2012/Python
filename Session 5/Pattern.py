'''
this loop run only till 8
for i in range(1,10):
    for j in range(1,i):
        print(j,end="")
    print()
'''

'''
this will run also till 9 cause we write +1
for i in range(1,10):
    for j in range(1,i+1):
        print(j,end="")
    print()
'''

'''
this will print same number  cause we give command only i
for i in range(1,10):
    for j in range(1,i):
        print(i,end="")
    print()
'''

for i in range(1,10):
    for j in range(0,i):
        print(i,end="")
    print()
