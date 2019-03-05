
def playagain():
    restart = input("Do you want to play again?(Y/N)")
    while restart not in ["N","n","Y","y"]:
        restart = str(input("Invalid input. Choose between Y and N:"))
    if restart in ["Y","y"]:
        restart = True
    elif restart in ["N","n"]:
        restart = False
    return restart

def beginning():
    #global P
    print("Welcome to Tic Tac Toe Game!!")
    while True:
        print("Player 1 please choose a symbol between X and O.")
        (P[1], P[2]) = player_setup()
        print("Player 1 just chose {}.".format(P[1]))
        confirm = int(input("Please enter 1 to confirm or enter 2 to reselect:"))
        if confirm == 1:
            print("Player 1 is {} and Player 2 is {}".format(P[1], P[2]))
            break
        else:
            pass


def player_setup():
    P1 = str(input("Please choose between X and O:"))
    while P1 not in ["X","x","O","o"]:
        PP1 = str(input("Invalid input. Choose between X and O:"))
    P1 = P1.upper()
    P2 = ""
    if P1 == "X":
        P2 = "O"
    else:
        P2 = "X"
    return (P1, P2)


def print_grid():
    print("  {}  |  {}  |  {}  ".format(grid[1], grid[2], grid[3]))
    print("_____|_____|_____")
    print("  {}  |  {}  |  {}  ".format(grid[4], grid[5], grid[6]))
    print("_____|_____|_____")
    print("  {}  |  {}  |  {}  ".format(grid[7], grid[8], grid[9]))
    print("     |     |     ")

def player_input():
    PP1 = 0
    PP2 = 0
    if grid[0] == 1:
        PP1 = int(input("Player 1 choose a non-occupied location (1-9) to place your symbol:"))
        while PP1 not in range(1,10):
            PP1 = int(input("Invalid input. Choose from (1-9):"))
        while occupied[PP1] != 0:
            PP1 = int(input("You may only choose non-occupied location. Please select again:"))

        grid[PP1] = P[1]
        occupied[PP1] = 1
        grid[0] = 2
    else:
        PP2 = int(input("Player 2 choose a non-occupied location (1-9) to place your symbol:"))
        while PP2 not in range(1,10):
            PP2 = int(input("Invalid input. Choose from (1-9):"))
        while occupied[PP2] != 0:
            PP2 = int(input("You may only choose non-occupied location. Please select again:"))

        grid[PP2] = P[2]
        occupied[PP2] = 2
        grid[0] = 1


def checkifwin():
    global winner
    if sum([occupied[1],occupied[2],occupied[3],]) == 6:
        winner = 2
    elif sum([occupied[4],occupied[5],occupied[6],]) == 6:
        winner = 2
    elif sum([occupied[7],occupied[8],occupied[9],]) == 6:
        winner = 2
    elif sum([occupied[1],occupied[4],occupied[7],]) == 6:
        winner = 2
    elif sum([occupied[2],occupied[5],occupied[8],]) == 6:
        winner = 2
    elif sum([occupied[3],occupied[6],occupied[9],]) == 6:
        winner = 2
    elif sum([occupied[1],occupied[5],occupied[9],]) == 6:
        winner = 2
    elif sum([occupied[3],occupied[5],occupied[7],]) == 6:
        winner = 2
    elif (sum([occupied[1],occupied[2],occupied[3],]) == 3) and (0 not in [occupied[1],occupied[2],occupied[3]]):
        winner = 1
    elif (sum([occupied[4],occupied[5],occupied[6],]) == 3) and (0 not in [occupied[4],occupied[5],occupied[6]]):
        winner = 1
    elif (sum([occupied[7],occupied[8],occupied[9],]) == 3) and (0 not in [occupied[7],occupied[8],occupied[9]]):
        winner = 1
    elif (sum([occupied[1],occupied[4],occupied[7],]) == 3) and (0 not in [occupied[1],occupied[4],occupied[7]]):
        winner = 1
    elif (sum([occupied[2],occupied[5],occupied[8],]) == 3) and (0 not in [occupied[2],occupied[5],occupied[6]]):
        winner = 1
    elif (sum([occupied[3],occupied[6],occupied[9],]) == 3) and (0 not in [occupied[3],occupied[6],occupied[9]]):
        winner = 1
    elif (sum([occupied[1],occupied[5],occupied[9],]) == 3) and (0 not in [occupied[1],occupied[5],occupied[9]]):
        winner = 1
    elif (sum([occupied[3],occupied[5],occupied[7],]) == 3) and (0 not in [occupied[3],occupied[5],occupied[7]]):
        winner = 1
    elif 0 not in occupied[1:10]:
        winner = 3




""" main function starts """
start = True
while start == True:
    P ={1:"", 2:""}  #declare player 1 and 2
    occupied = [0]*10
    beginning()    #let player1 select his/her symbol

    grid = [" "]*10
    for i in range(0,10):
        grid[i] = i
    print_grid()

    winner = 0     # to indicate if bingo
    grid[0] = 1     # to save memory, use it as  as an player indicator

    while winner == 0:
        player_input()
        print_grid()
        checkifwin()

    if winner == 1 or winner ==2:
        print("\nThe Winner Is: Player {} !!\n\nThanks for playing.".format(winner))
    elif winner == 3:
        print("\nGame Over!\nIt is a draw...".format(winner))

    start = playagain()
    if not start:
        break