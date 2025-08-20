import random, os, time, copy

"""
**********************
SLOT MACHINE FUNCTIONS
**********************
"""

Board = []

def create_board():
    Board_number = []
    Board_finished = []
    for numbers in range (0,15):
        Board_number.append(int((random.randint(1,16))))
    for number in Board_number:
        if number in range(1,7):
            Board_finished.append("X")
        elif number in range(7,14):
            Board_finished.append("?")
        elif number in range(14,16):
            Board_finished.append("$")
        else:
            Board_finished.append("*")
    return Board_finished
"""                        In Work (Maybe later)
def update_board(Board):
    Board_new_row_n = []
    Board_new_row = []
    Board_f = Board.copy()
    for numbers in range (0,3):
        Board_new_row_n.append(int((random.randint(1,16))))
    for number in Board_new_row_n:
        if number in range(0,6):
            Board_new_row.append("X")
        elif number in range(6,11):
            Board_new_row.append("?")
        elif number in range(11,15):
            Board_new_row.append("$")
        else:
            Board_new_row.append("*")
    for numbers in range (14,11):
        Board_f.pop(numbers)
    for numbers in range (0,3):
        Board_f.append(Board_new_row[numbers])   
    return Board_f.copy()
"""
def check_answer(Board,Bet):
    if Board[6] == Board[7] and Board[6] == Board[8]:
        if Board[6] == "X":
            print("You won 5x")
            Prise = Bet * 5
        elif Board[6] == "?":
            print("You won a Mystery prize")
            Prise = Bet * random.randint(2,14)
        elif Board[6] == "$":
            print("You won the Money Bag")
            Prise = Bet * 20
        elif Board[6] == "*":
            Prise = Bet * 100
    else:
        print("You didin't win")
        Prise = -abs(Bet)
    return Prise
def display_machine(Board):
    print("""                _________________
                | ------------- |
                | |XXXXXXXXXX$| |  ____
                | ------------- | |    |
                |  ____________ | |____|
                | | {} | {}|  {} | | / /
                | | {} | {}|  {} | |/ /            
                |>| {} | {}|  {} |<| /
                | | {} | {}|  {} | |/
                | | {} | {}|  {} | |
                | |___________| |
            ____|               |____
            |                        |
            |                        | 
            |                        |
            |                        |
            |                        |
            |                        |
            |                        |
            |                        |
            |________________________|            """.format(Board[0],Board[1],Board[2],Board[3],Board[4],Board[5],Board[6],Board[7],Board[8],Board[9],Board[10],Board[11],Board[12],Board[13],Board[14]))