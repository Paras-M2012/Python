#1. calculate_total — Positional Arguments
def calculate_total(price, quantity):
    return price * quantity

result = calculate_total(120, 3)
print(result)

#2. format_username — Optional Argument
def format_username(username, prefix='user_'):
    return prefix + username

print(format_username('kabir123'))

print(format_username('kabir123', prefix='pro_'))

#3. book_movie_ticket — Positional, Keyword, and Mixed Calls

def book_movie_ticket(movie_name, seat_type='Regular', snacks=None):
    print(f"Movie: {movie_name}")
    print(f"Seat Type: {seat_type}")
    print(f"Snacks: {snacks if snacks else 'None'}")
    print("-" * 30)


book_movie_ticket('Jawan', 'VIP', 'Popcorn')


book_movie_ticket(movie_name='Pathaan', seat_type='Premium', snacks='Nachos')


book_movie_ticket('Jawan', snacks='Popcorn', seat_type='VIP')

#4. apply_coupon — Conditional Discount with Default

def apply_coupon(amount, coupon_code=None):
    if coupon_code == 'SAVE10':
        discount = amount * 0.10
        final_amount = amount - discount
    else:
        final_amount = amount
    return final_amount

print(apply_coupon(1000))

print(apply_coupon(1000, coupon_code='SAVE10'))

print(apply_coupon(1000, coupon_code='SAVE20'))
