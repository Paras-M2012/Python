'''
1. Round cricket scores to nearest integer
'''
scores = [56.7, 102.3, 88.9, 45.2, 120.8]
rounded_scores = [round(score) for score in scores]

print("Original scores:", scores)
print("Rounded scores:", rounded_scores)

print()

'''
2. Sort restaurant ratings in descending order
'''
ratings = [4.2, 3.8, 4.9, 2.5, 4.0]
descending_ratings = sorted(ratings, reverse=True)

print("Ratings (descending):", descending_ratings)

print()

'''
3. Sort Flipkart product names alphabetically
'''
products = ['Wireless Mouse', 'Bluetooth Speaker', 'Laptop Stand', 'Phone Case', 'Keyboard']
products.sort()

print("Sorted products:", products)

print()

'''
4. Zip restaurants with delivery times
'''
restaurants = ['Burger Hub', 'Pizza Point', 'Sushi House']
delivery_times = [30, 25, 40]

for name, time in zip(restaurants, delivery_times):
    print(f"{name} - {time} min")

print()

'''
5. Function to pair YouTube titles with rounded view counts
'''
def get_video_stats(titles, views):
    return [(title, round(view, -3)) for title, view in zip(titles, views)]

titles = ["Python Tutorial", "Cooking Vlog", "Travel Diary"]
views = [125430, 87650, 302890]

video_stats = get_video_stats(titles, views)
print("Video stats:", video_stats)
