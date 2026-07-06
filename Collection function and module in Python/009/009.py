#1. Lambda function to calculate the square of a number

square = lambda x: x * x


for i in range(1, 9):
    print(f"Square of {i} =", square(i))


#2. Add a 10% service charge using map() and lambda()
prices = [120, 250, 99, 180, 310]

updated_prices = list(map(lambda price: price + (price * 0.10), prices))

print(updated_prices)

#3. Filter usernames with more than 1000 followers
users = [
    ('raj', 800),
    ('simran', 1500),
    ('veer', 1200),
    ('ananya', 950)
]

popular_users = list(filter(lambda user: user[1] > 1000, users))

print("Users with 'K' badge:")

for username, followers in popular_users:
    print(username)


#4. Lambda function to return sum and product as a tuple

calculate = lambda a, b: (a + b, a * b)

pairs = [(3, 4), (5, 2), (7, 8)]

for a, b in pairs:
    result = calculate(a, b)
    print(f"Numbers: {a}, {b}")
    print("Sum =", result[0])
    print("Product =", result[1])
    print()

#5. Lambda function to check if a string is a palindrome

palindrome = lambda text: text == text[::-1]

words = ["madam", "python", "noon"]

for word in words:
    print(word, "->", palindrome(word))
