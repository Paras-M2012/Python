class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email



user1 = User("paras123", "paras@gmail.com")


print("Username:", user1.username)
print("Email:", user1.email)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers



inf = Influencer("paras123", "paras@gmail.com", 25000)


print("Username:", inf.username)
print("Email:", inf.email)
print("Followers:", inf.followers)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge



v = VerifiedInfluencer(
    "paras123",
    "paras@gmail.com",
    500000,
    "Verified"
)

print("Username:", v.username)
print("Email:", v.email)
print("Followers:", v.followers)
print("Badge:", v.badge)



class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name


class BrandPartner(Influencer, Brand):
    def __init__(self, username, email, followers, brand_name):
        Influencer.__init__(self, username, email, followers)
        Brand.__init__(self, brand_name)


partner = BrandPartner(
    "paras123",
    "paras@gmail.com",
    120000,
    "Nike"
)

print("Username:", partner.username)
print("Followers:", partner.followers)
print("Brand:", partner.brand_name)
