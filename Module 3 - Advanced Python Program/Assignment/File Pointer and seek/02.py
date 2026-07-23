file = open("lyrics.txt", "w")

file.write("""Twinkle Twinkle Little Star,
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky.""")

file.close()

print("lyrics.txt created successfully.")

file = open("lyrics.txt", "r")

print("Before reading:", file.tell())

data = file.read(10)
print("First 10 Characters:", data)

print("After reading:", file.tell())

file.close()

def read_next_line(filename):
    file = open(filename, "r")
    file.seek(20)
    print(file.readline())
    file.close()




read_next_line("lyrics.txt")




file = open("orders.txt", "w")

file.write("Pizza\n")
file.write("Burger\n")
file.write("Biryani\n")
file.write("Pasta\n")
file.write("Cold Coffee\n")

file.close()

print("orders.txt created successfully.")

file = open("orders.txt", "r")

while True:
    order = file.readline()

    if order == "":
        break

    print("Order:", order.strip())
    print("Pointer Position:", file.tell())

file.close()



file = open("playlist.txt", "w")

file.write("Kesariya\n")
file.write("Believer\n")
file.write("Shape of You\n")
file.write("Perfect\n")
file.write("Tum Hi Ho\n")

file.close()

print("playlist.txt created successfully.")

file = open("playlist.txt", "r")
file.seek(0)


file.readline()
file.readline()

third_song = file.readline()

print("Third Song:", third_song.strip())

file.close()
