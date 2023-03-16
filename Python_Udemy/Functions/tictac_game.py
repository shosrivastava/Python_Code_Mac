board = ["  " for i in range(9)]

def printBoard():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def playerMove(icon):

    if icon == "X":
        number = 1
    elif icon == "0":
        number = 2

    print(f"Your turn Player {number}.\n")

    choice = int(input("Enter your choice between 1 and 9.\n").strip())

    if board[choice - 1] == "  ":
        board[choice - 1] = icon
    else:
        print("This position has already been filled.\n")

def isVictory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True

    else:
        return False

while True:
    printBoard()
    playerMove("X")
    printBoard()
    if isVictory("X"):
        print("Congratulations, player X for winning the game!")
        break
    playerMove("0")
    if isVictory("0"):
        print("Congratulations player 0 for winning the game!")
        break