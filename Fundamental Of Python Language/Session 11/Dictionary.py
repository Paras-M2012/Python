'''
dictionary will always write in curly bracket.
Dictionary : there is only one unique but have multiple values.
you can find data only and only with the key.
there is multiple types of library function.
if you have to get any key than they have 2 types
1: find direct and write key in square bracket
2: use the get function.
'''
d={101:"Paras", 202:"Riya", 303:"Mantra", 456:"Sanjay", 688:"Hiral", 999:"Khushboo"}

print(d)
print(d[101])
print(d.get(688))
print(d.items())
print(d.keys())
print(d.values())
'''
this will get error
'''
print(d.pop(303))
print(d)
'''
with this delet last key and value both
'''
print(d.popitem())
print(d)
d1={404:"Siya", 505:"Dhyana"}
d.update(d1)
print(d)
for i in d:
    print(i, " : ", d[i])
