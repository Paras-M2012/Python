'''
Tuple will always write in Round Bracket
You can add list in tupple with append fucntion
There is only 2 types of tuple
1) Count
2) Index
''' 

t=(1,2,1.1,2.2,10,[100,200,300],20,"tops",False,1,2)


print(t)
print(t.count(1))
print(t.index(20))
for i in t:
    print(i)
t[5].append(400)
print(t)
