class InvalidCouponCodeError(Exception):
    pass


def apply_coupon(coupon_code):
    valid_coupons = ["SAVE50", "FOOD20", "WELCOME10"]

    if coupon_code not in valid_coupons:
        raise InvalidCouponCodeError("Invalid Coupon Code!")

    print("Coupon Applied Successfully.")


try:
    apply_coupon("SAVE50")
    apply_coupon("DISCOUNT100")

except InvalidCouponCodeError as e:
    print(e)




class SongAlreadyExistsError(Exception):
    pass



def add_song_to_playlist(song_name, playlist):

    if song_name in playlist:
        raise SongAlreadyExistsError("Song already exists in the playlist!")

    playlist.append(song_name)
    print(f"{song_name} added successfully.")


playlist = ["Believer", "Kesariya", "Perfect"]

try:
    add_song_to_playlist("Shape of You", playlist)
    add_song_to_playlist("Believer", playlist)

except SongAlreadyExistsError as e:
    print(e)

print("Playlist:", playlist)



# Custom Exception
class PaymentFailedError(Exception):
    pass


# Function
def process_payment(amount):

    if amount <= 0:
        raise PaymentFailedError("Payment Failed! Amount must be greater than zero.")

    print("Payment Successful")


# Main Program
try:
    process_payment(1500)
    process_payment(-500)

except PaymentFailedError as e:
    print(e)


class InvalidSeatNumberError(Exception):
    pass


def book_ticket(movie_name, seat_number):

    if seat_number <= 0:
        raise InvalidSeatNumberError("Seat number must be positive")

    print("Ticket Booked Successfully")


try:
    book_ticket("Avengers", -2)

except InvalidSeatNumberError as e:
    print(e)
