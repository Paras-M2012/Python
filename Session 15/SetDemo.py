# Using Curly Braces
my_set = {1, 2, 3, 4, 5, 8, 10, 25}

#Using The Set as a () Constructor
my_set2 = set([1, 2, 3, 4, 9])


print(my_set)
print(my_set2)

my_set.remove(2)
print(my_set)

my_set.add(38)
print(my_set)
print(my_set2)

print(my_set2.difference(my_set))
print(my_set.intersection(my_set2))
print(my_set.union(my_set2))
