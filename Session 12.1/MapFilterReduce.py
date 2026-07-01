from functools import reduce

# 1. Function to calculate discounted price
def get_discounted_price(price, discount_percent):
    final_price = price - (price * discount_percent / 100)
    return final_price

# Test
print("Discounted Price:", get_discounted_price(500, 10))


# 2. Function to format follower count
def format_follower_count(number):
    if number >= 1000000:
        return f"{number / 1000000:.1f}M"
    elif number >= 1000:
        return f"{number / 1000:.1f}K"
    else:
        return str(number)

# Test
print("1500 ->", format_follower_count(1500))
print("1200000 ->", format_follower_count(1200000))
print("850 ->", format_follower_count(850))


# 3. Convert song durations from minutes to seconds
song_durations = [3, 4, 5, 6]

seconds = list(map(lambda x: x * 60, song_durations))

print("Song Durations in Seconds:", seconds)


# 4. Filter product names starting with 'M'
products = ["Mobile", "Mouse", "Laptop", "Monitor", "Keyboard"]

m_products = list(filter(lambda x: x.startswith("M"), products))

print("Products Starting with M:", m_products)


# 5. Calculate total bill using reduce()
prices = [120, 80, 150, 60]

total_bill = reduce(lambda x, y: x + y, prices)

print("Total Bill:", total_bill)
