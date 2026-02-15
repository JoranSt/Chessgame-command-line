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
            move = input("Enter move in the form of B1D1\n")
            movesplit = list(move)
            print(movesplit)
            try:
                coordinates = self.board.unicode_to_index(movesplit)
                print(self.board.move_piece([coordinates[0],coordinates[1]], [coordinates[2],coordinates[3]], self.turn))
                self.turn = "black" if self.turn == "white" else "white"
            except:
                print("Input unvalid please try again")

    


chessgame = Chess(board)
chessgame.play()
        

