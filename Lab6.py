# Defines a function to encode a password
def encode(password):
    encoded_password = ""  # Store the encoded password here

    # Loop through each digit in the password
    for digit in password:
        # Convert the digit to a number, add 3, and ensure it's a single digit
        encoded_digit = (int(digit) + 3) % 10
        # Add the encoded digit to the encoded password
        encoded_password += str(encoded_digit)

    return encoded_password

# Function to decode the password
def decode(encoded_password):
    decoded_password = ""  # We'll store the decoded password here

    # Loop through each digit in the encoded password
    for digit in encoded_password:
        # Convert the digit to a number, subtract 3, handle negative numbers, and ensure it's a single digit
        decoded_digit = (int(digit) - 3 + 10) % 10
        # Add the decoded digit to the decoded password
        decoded_password += str(decoded_digit)

    return decoded_password

# Main function to drive the program
def main():
    while True:
        print("\nMenu:")
        print("1. Encode password")
        print("2. Decode password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Ask the user for an 8-digit password to encode
            password = input("Enter the 8-digit password to encode: ")
            # Validate the password
            if len(password) != 8 or not password.isdigit():
                print("Invalid password. Please enter an 8-digit password containing only numbers.")
                continue
            # Encode the password and display it
            encoded_password = encode(password)
            print("Encoded password:", encoded_password)
        elif choice == '2':
            # Ask the user for the encoded password to decode
            encoded_password = input("Enter the encoded password to decode: ")
            # Validate the encoded password
            if len(encoded_password) != 8 or not encoded_password.isdigit():
                print("Invalid encoded password. Please enter an 8-digit password containing only numbers.")
                continue
            # Decode the password and display it
            decoded_password = decode(encoded_password)
            print("Decoded password:", decoded_password)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Call the main function to start the program
if __name__ == "__main__":
    main()