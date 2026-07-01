# 1. Create a dictionary with songs and durations
my_playlist = {
    "Shape of You": 4.2,
    "Believer": 3.5,
    "Perfect": 4.4
}

print("My Playlist:")
print(my_playlist)

# 2. Add a new song and update an existing song
my_playlist["Blinding Lights"] = 3.3      # Add new song
my_playlist["Believer"] = 3.8             # Update duration

print("\nUpdated Playlist:")
print(my_playlist)


# 3. Function to display Instagram followers
def display_friends(friends):
    for username, followers in friends.items():
        print(f"{username}: {followers} followers")


friends = {
    "Paras": "2.3K",
    "Rahul": "5K",
    "Riya": "1.8K"
}

print("\nInstagram Followers:")
display_friends(friends)


# 4. Dictionary methods: keys(), values(), items()
food_order = {
    "Pizza": 2,
    "Burger": 1,
    "Fries": 3
}

print("\nFood Items:")
print(food_order.keys())

print("\nQuantities:")
print(food_order.values())

print("\nItems with Quantities:")
for item, qty in food_order.items():
    print(item, ":", qty)


# 5. Function to update shopping cart
def update_cart(cart, item, qty):
    if item in cart:
        cart[item] += qty      # Increase quantity
    else:
        cart[item] = qty       # Add new item
    return cart


cart = {
    "Laptop": 1,
    "Mouse": 2
}

updated_cart = update_cart(cart, "Keyboard", 1)
updated_cart = update_cart(updated_cart, "Mouse", 1)

print("\nUpdated Cart:")
print(updated_cart)
