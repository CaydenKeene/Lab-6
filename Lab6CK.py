# encoder function, author: Cayden Keene
def encoder(password):
    encoded_password = ""
    for i in password:
        i = int(i)
        i += 3
        if i > 9:
            i -= 10
        encoded_password += str(i)
    return encoded_password

# main function, author: Cayden Keene
if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")

        elif user_input == 2:
            decoder(encoded_password, password)

        elif user_input == 3:
            break
