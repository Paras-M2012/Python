file = open("my_fav_songs.txt", "w")

file.write("Kesariya\n")
file.write("Shape of You\n")
file.write("Believer\n")
file.write("Perfect\n")
file.write("Apna Bana Le\n")

file.close()

print("5 songs written successfully.")

file = open("my_fav_songs.txt", "r")

line_number = 1

for song in file:
    print(f"{line_number}. {song.strip()}")
    line_number += 1

file.close()

file = open("my_fav_songs.txt", "a")

file.write("Tum Hi Ho\n")
file.write("Blinding Lights\n")

file.close()

print("2 songs added successfully.")


file = open("my_fav_songs.txt", "r")

songs = file.readlines()

file.close()

for i, song in enumerate(songs, start=1):
    print(f"{i}. {song.strip()}")

print("Total songs:", len(songs))
