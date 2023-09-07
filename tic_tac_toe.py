import numpy
import random
board=numpy.array([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
p1s=random.choice("XO")
p2s="X" if p1s=="O" else "X"
class TicTacToe:
    def __init__(self,Player1= None ,Player2= None ) -> None:
        self.P1="Unknown 1" if Player1 is None else Player1
        self.P2="Unknown 2" if Player2 is None else Player2

    def display_board(self):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(board[0][0], board[0][1], board[0][2]))
        print('\t_____|_____|_____')
    
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(board[1][0], board[1][1], board[1][2]))
        print('\t_____|_____|_____')
    
        print("\t     |     |")
    
        print("\t  {}  |  {}  |  {}".format(board[2][0], board[2][1], board[2][2]))
        print("\t     |     |")
        print("\n")

    def check_row(self,symbol : str) -> bool:
        for r in range(3):
            count=0
            for c in range(3):
                if board[r][c]==symbol:
                    count+=1
            if count==3:
                return True 
        return False

    def check_col(self,symbol : str) -> bool:
        for c in range(3):
            count=0
            for r in range(3):
                if board[r][c]==symbol:
                    count+=1
            if count==3:
                return True
        return False

    def check_diag(self,symbol : str) -> bool:
        if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
            return True
        if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
            return True
        return False

    def won(self,symbol : str) -> bool:
        return self.check_row(symbol) or self.check_col(symbol) or self.check_diag(symbol)

    def place(self,symbol : str) -> bool:
        self.display_board()
        while(1):
            row=int(input("Enter row ::: 1 or 2 or 3 -------- "))
            col=int(input("Enter coloumn ::: 1 or 2 or 3 ---- "))
            print("\n")
            if row>0 and row<4 and col<4 and col>0 and board[row-1][col-1]==' ':
                break
            else:
                print("Invalid input! Enter valid choice.")
            print("===============================================\n")
        board[row-1][col-1]=symbol

    def play(self,symbol1: str, symbol2: str) -> None:
        for turn in range(9):
            print("===============================================\n")
            if turn%2==0:
                print(f"{self.P1}'s turn")
                self.place(symbol1)
                if self.won(symbol1):
                    self.display_board()
                    print(symbol1,"Won !")
                    break
            elif turn%2!=0:
                print(f"{self.P2}'s turn")
                self.place(symbol2)
                if self.won(symbol2):
                    self.display_board()
                    print(symbol2,"Won !")
                    break
        if not(self.won(symbol1)) and not(self.won(symbol2)):
            self.display_board()
            print("DRAW!!")

if __name__ == "__main__":
    print("===============================================")
    Player1=input("Enter Player 1's Name. Press Enter for annonymous: ")
    Player2=input("Enter Player 2's Name. Press Enter for annonymous: ")

    if Player1 and Player2:
        obj= TicTacToe(Player1,Player2) #if both player provide their names
    elif not Player1 and not Player2:
        obj= TicTacToe() #if none provide their name
    else:
        obj = TicTacToe(Player1) if Player1 and not Player2 else TicTacToe(Player2=Player2) #if either of the 2 provide their name

    print(f"\n{obj.P1} got symbol X and will go first.") if p1s=='X' else print(f"{obj.P2} got symbol X and will go first.\n")
    print("{} and {} Let's play!!!!!!".format(obj.P1,obj.P2))
    print("\nStart the game!!")

    obj.play('X','O') if p1s=='X' else obj.play('O','X')