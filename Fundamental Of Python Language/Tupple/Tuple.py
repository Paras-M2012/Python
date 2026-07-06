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



# 1. Create a tuple and print it
fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")

print("Favorite Apps:", fav_apps)

# 2. Access and print the 2nd and 4th app names
print("2nd App:", fav_apps[1])
print("4th App:", fav_apps[3])

# 3. Try to change the first element
# fav_apps[0] = "YouTube"   # This will raise a TypeError

# Explanation:
# Tuples are immutable, which means their elements cannot be
# changed, added, or removed after the tuple is created.

# 4. Print the middle three app names using slicing
print("Middle Three Apps:", fav_apps[1:4])

# 5. Create another tuple and concatenate
new_apps = ("ChatGPT", "Amazon")

all_apps = fav_apps + new_apps

print("All Apps:", all_apps)
