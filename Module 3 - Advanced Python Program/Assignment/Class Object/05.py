class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


song1 = Song("Believer", "Imagine Dragons", 204)
song2 = Song("Kesariya", "Arijit Singh", 268)


print("Song 1")
print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration, "seconds")

print()

print("Song 2")
print("Title:", song2.title)
print("Artist:", song2.artist)
print("Duration:", song2.duration, "seconds")



class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def show_order(self):
        print("Restaurant:", self.restaurant_name)
        print("Items:", ", ".join(self.items))
        print("Total Price: ₹", self.total_price)


order = FoodOrder(
    "Domino's",
    ["Pizza", "Garlic Bread", "Coke"],
    850
)

order.show_order()


class InstagramPost:
    def __init__(self, caption, likes, comments):
        self.caption = caption
        self.likes = likes
        self.comments = comments

    def add_comment(self, comment_text):
        self.comments.append(comment_text)
        self.likes += 1



post = InstagramPost(
    "Enjoying my vacation!",
    120,
    ["Nice!", "Awesome Pic!"]
)
post.add_comment("Beautiful View!")


print("Caption:", post.caption)
print("Likes:", post.likes)
print("Comments:", post.comments)




class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating


m = Movie("Jawan", 4.5)

print(m.title)
print(m.rating)
