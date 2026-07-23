def get_song_duration(song_name):
    songs = {
        "Kesariya": "4:28",
        "Believer": "3:24",
        "Shape of You": "3:53",
        "Perfect": "4:40",
        "Tum Hi Ho": "4:22"
    }

    try:
        print("Duration:", songs[song_name])
    except KeyError:
        print("Song not found on Spotify!")


# Function Calls
get_song_duration("Believer")
get_song_duration("Despacito")



try:
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity

    print("Total Amount = ₹", total)

except ValueError:
    print("Error: Please enter only numeric values.")



def book_movie_ticket():
    wallet_balance = 1000

    try:
        tickets = int(input("Enter number of tickets: "))

        price_per_ticket = wallet_balance / tickets

        print("Price per Ticket = ₹", price_per_ticket)

    except ZeroDivisionError:
        print("Error: Number of tickets cannot be zero.")

    except ValueError:
        print("Error: Please enter a valid number.")


book_movie_ticket()


my_list = [1, 2, 3]
my_dict = {'a': 1}

# Handle IndexError
try:
    print(my_list[5])
except IndexError:
    print("Error: List index is out of range.")

# Handle KeyError
try:
    print(my_dict['b'])
except KeyError:
    print("Error: Key not found in dictionary.")
