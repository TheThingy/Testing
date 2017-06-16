from random import randint
score = [0, 0]
choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
while True:
    computer_input = str(randint(1, 9))
    user_input = str(input("Enter guess between 1-9: "))

    if user_input == "exit":
        print(user_input)
        print("You have won %d times and lost %d times" % (score[0], score[1]))
        print("Total games: %d" % (score[0] + score[1]))
        break

    if user_input in choices:
        if user_input == computer_input:
            print("You win!")
            score[0] += 1
        else:
            print("You loose")
            print("The computer chose: %s" % (computer_input))
            score[1] += 1
    else:
        print("Please enter a number or 'exit'")


