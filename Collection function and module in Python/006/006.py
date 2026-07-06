#1. Products & Prices with zip()

products = ["Notebook", "Pen", "Water Bottle"]
prices = [120, 15, 350]

product_prices = dict(zip(products, prices))

print(product_prices)

#2. Usernames & Followers (Manual Loop, No zip())

usernames = ["raj_07", "ananya_xo", "kabir.codes"]
followers = [1500, 8200, 640]

user_followers = {}

for i in range(len(usernames)):
    user_followers[usernames[i]] = followers[i]

print(user_followers)

#3. IPL Teams — Filter by Points
teams = ["CSK", "MI", "GT", "RCB", "KKR"]
points = [16, 8, 18, 10, 14]

team_points = dict(zip(teams, points))

print(team_points)

print("\nTeams with more than 10 points:")
for team, pts in team_points.items():
    if pts > 10:
        print(f"{team}: {pts}")


#4. Movies — List of Dictionaries
titles = ["Pathaan", "12th Fail", "Jawan"]
genres = ["Action", "Drama", "Action"]
ratings = [7.8, 8.9, 7.5]

movies = []

for title, genre, rating in zip(titles, genres, ratings):
    movie_dict = {"title": title, "genre": genre, "rating": rating}
    movies.append(movie_dict)

print(movies)



