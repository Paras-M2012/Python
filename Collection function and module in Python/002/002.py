'''
1. Playlist with position numbers
'''
playlist = ["The Kerela Story", "Oh My God!", "Ankur Arora - The Murder Case", "Asur", "Chaal Jivi Laiye"]

for i in range(len(playlist)):
    print(f"{i + 1}. {playlist[i]}")

print()

'''
2. Print first three food items using range()
'''
foods = ['Pizza', 'Burger', 'Dosa', 'Pasta', 'Fries']

for i in range(3):
    print(foods[i])

print()

'''
3. Flipkart cart total value
'''
prices = [299, 499, 150, 1200, 350]
total = 0

for price in prices:
    total += price

print("Total cart value:", total)

print()

'''
4. WhatsApp-style unread messages counter
'''
unread_counts = [2, 0, 15, 120, 5]

for count in unread_counts:
    if count > 99:
        print("99+")
    else:
        print(count)
