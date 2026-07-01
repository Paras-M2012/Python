'''
In file management there is total 3 mode W R A
write read append
Write will make automatically new file with .txt
'''


file=open("Tops1.txt" , "w")
file.write("This is File management demo using python")
file.close()
print("File Written Successfully")
print("-"*70)

file=open("Tops1.txt", "r")
print(file.read())
file.close()
print("-"*70)


file=open("Tops1.txt", "a")
file.write("\nThis file is now appended.")
file.close()
print("File Appended.")
print("-"*70)


file=open("Tops1.txt","r")
print(file.read())
file.close()
print("-"*70)

file=open("Tops2.txt","w+")
file.write("This is w+ mode using python.")
print("File Current Position : ",file.tell())
file.seek(0)
print("File Data : ", file.read())
file.close()
print("-"*70)
    
    
