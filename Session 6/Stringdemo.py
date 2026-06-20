s="Tops Technologies"

print(s)
'''
first letter will be capital
'''
print(s.capitalize())

''''
All letter will be Small
'''
print(s.casefold())

'''
All capital
'''
print(s.upper())

'''
capital convert in small and small convert into capital
'''
print(s.swapcase())

'''
in this case you have to give any types of specific symbole and width so text well in center and before and after that will be print symbole
'''
print(s.center(50,"-"))

'''
This will specific word counter if you give any word than it will be count how much total word in this sentence
'''
print(s.count("o"))

'''
bullen function will answer always in true or false.
will ask to string your string will end with es than true otherwise false.
same in startwith
'''
print(s.endswith("is"))
print(s.startswith("tops"))

'''
Find is find the word from the string that will find our word in which index
'''
print(s.find("log"))

'''
find index Number. if you give any specific number that it will start count from there.
'''
print(s.index("T",2))

'''
is function is always bullen so give answer in true and false
isalnum (is alpha numeric)
alpha true
numeric true
both true
space is false cause that in not alphanumeric
'''
print("tops123".isalnum())
print("tops".isalnum())
print("123".isalnum())

'''

'''
print("123".isnumeric())
print("tops".isalpha())

'''
as per english grammer title is always first letter will be capital.
isspace means in sentence have space than true
'''
print(s.istitle())
print(" ".isspace())
print("tops".islower())
print("TOPS".isupper())
print("Hello".replace("l","w"))

'''
if you wtite in small letter and give a title than it will transform first letter in capital
'''
print("naroda orthopedic hospital".title())


