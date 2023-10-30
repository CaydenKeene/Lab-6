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

def decoder(ep):
    p = ""
    for i in ep:
        if int(i)-3 <= 0:
            print("ERROR")
            break
        else:
            p = p + str(int(i)-3)
    return p

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
            password = decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {password}.\n")
        elif user_input == 3:
            break
