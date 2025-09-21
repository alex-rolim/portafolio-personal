# Import the necessary modules
import random
import string

# Define the characters that will be used to generate the password
# string.ascii_letters includes lowercase and uppercase letters
# string.digits includes numbers from 0 to 9
# string.punctuation includes special characters (!@#$%, etc.)
characters = string.ascii_letters + string.digits + string.punctuation

# Ask the user what length they want for the password
password_length = int(input("Enter the desired password length: "))

# Generate the password
# random.choice() chooses a random character from the list
# The 'for' loop repeats this action the number of times indicated by the user
generated_password = "".join(random.choice(characters) for i in range(password_length))

# Print the password on the screen

print("Your new password is: ", generated_password)
