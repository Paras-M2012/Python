#1. Square Roots with math.sqrt()

import math

numbers = [16, 49, 81]

for num in numbers:
    print(f"Square root of {num} is {math.sqrt(num)}")

#2. Flipkart-style Price Rounder with math.ceil()

import math

prices = [199.1, 349.8, 599.3]

rounded_prices = []
for price in prices:
    rounded_prices.append(math.ceil(price))

print(rounded_prices)


#3. Zomato Bill Calculator with math.floor()
import math

bill_amount = 1138
discount_percent = 10

discount = bill_amount * (discount_percent / 100)
final_amount = bill_amount - discount

final_bill = math.floor(final_amount)

print(f"Original Bill: ₹{bill_amount}")
print(f"Discount: ₹{discount}")
print(f"Final Bill (rounded down): ₹{final_bill}")


#4. Dice Roll Simulator
import random

dice_result = random.randint(1, 6)
print(f"You rolled a {dice_result}!")

#5. Spotify-style Playlist Shuffle with random.sample()

import random

songs = [
    "Kesariya", "Apna Bana Le", "Tum Hi Ho", "Chaiyya Chaiyya",
    "Kar Har Maidaan Fateh", "Zinda", "Rockstar", "Ilahi"
]

todays_playlist = random.sample(songs, 3)

print("Today's Playlist:")
for song in todays_playlist:
    print(f"- {song}")
