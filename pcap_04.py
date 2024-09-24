from random import randrange
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
free_fields = []
free_spots = []

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    b = board
    print("""
    +-------+-------+-------+
    |       |       |       |
    |   {}   |   {}   |   {}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {}   |   {}   |   {}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {}   |   {}   |   {}   |
    |       |       |       |
    +-------+-------+-------+
    """.format(b[0][0], b[0][1], b[0][2], b[1][0], b[1][1], b[1][2], b[2][0], b[2][1], b[2][2]))

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    b = board
    valid_move = False
    while valid_move == False:
        try:
            move = int(input("Enter your move: "))
        except ValueError:
            print("Not a number, enter a number from 1 to 9.")
            continue
        if move not in range(1, 10):
            print("Invalid number, enter a number from 1 to 9.")
            continue
        if move not in free_spots:
            print("Invalid move, enter a number available in the board")
            continue
        else:
            valid_move = True

    for i in range(0, 3):
        for j in range(0, 3):
            if move == b[i][j]:
                b[i][j] = "O"
    
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    b = board
    global free_spots, free_fields
    free_spots.clear()
    for i in range(0, 3):
        for j in range(0, 3):
            if b[i][j] not in ["X", "O"]:
                free_fields.append((i, j))
                free_spots.append(b[i][j])
                
    #print(free_spots)

def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    b = board
    for i in range(0, 3):
        if b[i][0] == b[i][1] == b[i][2]:
            if b[i][0] == "O":
                print("You won!")
            else:
                print("Computer won.")
            return True
        elif b[0][i] == b[1][i] == b[2][i]:
            if b[0][i] == "O":
                print("You won!")
            else:
                print("Computer won.")
            return True
        else:
            return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    b = board
    valid_move = False
    while valid_move == False:
        move = randrange(1,10)
        if move in free_spots:
            for i in range(0, 3):
                for j in range(0, 3):
                    if move == b[i][j]:
                        b[i][j] = "X"
                        valid_move = True
        continue
    
    #print(move)

# first_move
board[1][1] = "X"

while victory_for(board) == False:
    display_board(board)
    make_list_of_free_fields(board)
    enter_move(board)
    display_board(board)
    victory_for(board)
    if victory_for(board) == True:
    	break
    make_list_of_free_fields(board)
    draw_move(board)
    display_board(board)
    victory_for(board)
    
