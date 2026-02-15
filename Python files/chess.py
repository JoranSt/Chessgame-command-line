from chessPieces import *
from board import Board

board = Board()


class Chess:
    def __init__(self, board, turn = "white"):
        self.board = board
        self.turn = turn
    
    def play(self):
        while True:
            self.board.display_board()
            #checks if the side whos turn it is is checked
            check = self.board.is_check(self.turn)
            print(check)
            move = input("Enter move in the form of B1D1\n")
            movesplit = list(move)

            try:
                #splits the input and gives itto the move piece function in the board class
                coordinates = self.board.unicode_to_index(movesplit)
                print(self.board.move_piece([coordinates[0],coordinates[1]], [coordinates[2],coordinates[3]], self.turn))
                self.turn = "black" if self.turn == "white" else "white"
                print("\n")
            except:
                print("Input unvalid please try again")

    


chessgame = Chess(board)
chessgame.play()
        

