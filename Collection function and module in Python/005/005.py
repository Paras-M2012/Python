#1
playlist = {
    "Kesariya": 268,
    "Apna Bana Le": 231,
    "Shape of You": 233
}

# Update the duration of one song
playlist["Kesariya"] = 240

print(playlist)


#2
user_profiles = {
    "paras_11": {
        "followers": 1500,
        "following": 300,
        "posts": 45
    },
    "sanjay_04": {
        "followers": 8200,
        "following": 512,
        "posts": 132
    }
}

print(user_profiles["sanjay_04"]["followers"])


#3
restaurants = {
    "Madhav Orchid": {"cuisine": "Gujarati", "rating": 4.2},
    "Domino's": {"cuisine": "Pizza", "rating": 4.5}
}

# Update the rating of one restaurant
restaurants["Madhav Orchid"]["rating"] = 4.6

print(restaurants)


#4
team = {
    'CSK': {'captain': 'MS Dhoni', 'players': 18},
    'MI': {'captain': 'Rohit Sharma', 'players': 17}
}


team['GT'] = {'captain': 'Shubhman Gill', 'players': 16}

for team_name, details in team.items():
    print(f"{team_name}: {details['captain']}")


