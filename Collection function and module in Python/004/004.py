# Profile Create

my_profile = (" Paras ", 30, " Panchal ", True)
print(" My Profile : ", my_profile)


#slice

playlist = (' Bhajan ', ' Chalisa ',' Bollywood Songs ', ' Hindi Songs ',' Gujarati Songs') 
print("2nd ,3rd ,4th Songs : ", playlist[1:4])


# Tuple to List, add item, back to tuple

order = ("Diet Cock", "Green Salad Bowl", "Mojito")
order_list = list(order)
order_list.append("Broccoli")
order = tuple(order_list)

print("Your Final Order List Is Here : ", order)

# Mixed Tupple

insta_post = (101, 102, 103, "Paras Code", 104, ["python", "coding", "tech"], True)

print("Insta Post : ", insta_post)
for item in insta_post:
    print(f"{item} -> {type(item)}")
