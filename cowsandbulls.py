import random
def main():


    attempts = 0
    while True:
        try:
            computer = random.randint(1234, 9876)
            if dupechecker(computer) == 1:
                raise ValueError
        except ValueError:
            pass
        else:
            print(computer)
            break

    # Player input loop
    while True:
        try:
            # Fetching the user input
            user_input = input("Enter 4 unique numbers:\n")
            # checking the length of the user input
            if len(user_input) < 4 or len(user_input) > 4:
                raise ValueError
            # checking if the string has dupe values
            elif dupechecker(user_input) == 1:
                raise ValueError
        # Error if input is wrong
        except ValueError:
            print("Try again")

        else:
            # adds +1 each attempt
            attempts += 1

            break



def dupechecker(n):
    if len(str(n)) == len(set(str(n))):
        return 0
    else:
        return 1

def compare(computer, user_input):
    pass


if __name__ == '__main__':
    main()
