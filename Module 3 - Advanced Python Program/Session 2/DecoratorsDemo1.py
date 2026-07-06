# Decorator for validating the name and contact number
def validate_name_and_contact(func):
    def wrapper(name, contact_number):
        # Validate that the name is not empty and is a string
        if not name or not isinstance(name, str):
            return "Name must be a non-empty string."
        
        # Validate that the contact number is a 10-digit number (without using regex)
        if len(contact_number) != 10 or not contact_number.isdigit():
            return "Contact number must be a 10-digit number."
        
        # If both validations pass, call the original function
        return func(name, contact_number)
    return wrapper

# Function to register user details
@validate_name_and_contact
def register_user(name, contact_number):
    return f"User {name} with contact number {contact_number} has been successfully registered."

name=input("Enter Your Name : ")
contact=input("Enter Your 10 Digit Contact Number : ")


# Testing the function with valid and invalid inputs
print(register_user(name, contact))  # Valid input

