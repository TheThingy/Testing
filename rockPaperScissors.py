choices = ["rock", "paper", "scissor"]
while True:
    player1 = str(input("Player 1, enter rock, paper or scissor: "))
    player2 = str(input("Player 2, enter rock, paper or scissor: "))

    if player1 or player2 == "rock" or "paper" or "scissor":
        if player1 == player2:
            print("It's a draw")
        elif player1 == "rock":
            if player2 == "paper":
                print("Player 2 wins")
            else:
                print("Player 1 wins")

        elif player1 == "paper":
            if player2 == "scissor":
                print("Player 2 wins")
            else:
                print("Player 1 wins")

        elif player1 == "scissor":
            if player2 == "rock":
                print("Player 2 wins")
            else:
                print("Player 1 wins")



