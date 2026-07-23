class InstaStory:
    def share(self):
        print("Sharing an image story")


class WhatsAppStory(InstaStory):
    def share(self):
        print("Sharing a text status")


insta = InstaStory()
whatsapp = WhatsAppStory()

insta.share()
whatsapp.share()


class Payment:
    def pay(self, amount):
        print("Paying", amount)


class UPI(Payment):
    def pay(self, amount):
        print("Paying", amount, "via UPI")

payment = Payment()
upi = UPI()

payment.pay(1000)
upi.pay(1000)


class ZomatoOrder:

    def add_item(self, item_name, quantity=1):
        print("Item:", item_name)
        print("Quantity:", quantity)
        print()


order = ZomatoOrder()

order.add_item("Pizza")

order.add_item("Burger", 3)


class Content:
    def display(self, title):
        print("Title:", title)


class Movie(Content):
    def display(self, title, year):
        print("Title:", title)
        print("Year :", year)

movie = Movie()

movie.display("Jawan", 2023)


class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")



email = EmailNotification()
sms = SMSNotification()

email.send()
sms.send()
