from chessPieces import *
from board import Board
import os
#Om te kijken of de koning schaak staat maak ik een functie aan die na het bewegen de valid_moves method aanroept
# Die functie past dan of de check attribute aan of kijkt naar of de koning op een valid_moves vlak staat
# Ook kan je voor elke beurt checken of the koning schaak staat door te kijken welke stukken die tegenkomt. 
#Bijvoorbeeld, koning h5 niks tussen h5 en h1 dus staat hij schaak (aannemend dat het verschillende kleuren zijn)
# vervolgens check alle stukkune of die schaak zetten en bepaal dan welke moves mogelijk zijn om uit schaak te komen indien geen moves schaakmat
board = Board()


class Chess:
    def __init__(self, board, turn = "white"):
        self.board = board
        self.turn = turn
        self.board.display_board()
    
    def play(self):
        while True:
            
            #checks if the side whos turn it is is checked
            # check = self.board.is_check(self.turn)
            # print(check)
            #check if king is checked
            move = input("Enter move in the form of B1D1\n")
            movesplit = list(move)
            #splits the input and gives itto the move piece function in the board class
            coordinates = self.board.unicode_to_index(movesplit)

            try:
                isvalid = self.board.move_piece([coordinates[0],coordinates[1]], [coordinates[2],coordinates[3]], self.turn)
                
            except:
                print("Input unvalid please try again")
                return
            
            if(isvalid == True):
                    self.turn = "black" if self.turn == "white" else "white"
                    color, piece = self.board.piece_info([coordinates[2],coordinates[3]])
                    from_, to_ = movesplit[:2], movesplit[2:]
                    os.system('cls')
                    print(self.board.is_check(self.turn))
                    print(f"{color} {piece} moved from {from_[0]}{from_[1]} to {to_[0]}{to_[1]}")
                    print("\n")
                    self.board.display_board()
            else:
                print("Cannot make this move")

    

if __name__ =="__main__":
    chessgame = Chess(board)
    chessgame.play()
        

