from chessPieces import *
from board import Board
import os

board = Board()


class Chess:
    def __init__(self, board, turn = "white"):
        self.board = board
        self.turn = turn
        os.system('cls')
        self.board.display_board()
    
    def play(self):
        while True:
                
            
            
            move = input("Enter move in the form of B1D1\n")
            movesplit = list(move)
            #splits the input and gives itto the move piece function in the board class
            coordinates = self.board.unicode_to_index(movesplit)

            try:
                result = self.board.move_piece([coordinates[0],coordinates[1]], [coordinates[2],coordinates[3]], self.turn)
                
            except:
                print("Input unvalid please try again")
                continue
            
            
            messages = {
                        "no_piece": "No piece at that square.",
                        "wrong_turn": "That's not your piece.",
                        "invalid_target": "That piece can't move there.",
                        "king_in_check": "You can't leave your king in check.",
                        "can't move through check": "You can't move through check"
                    }
            if(result == "ok"):
                    self.turn = "black" if self.turn == "white" else "white"
                    #checks for endgame
                    if self.board.checkmate(self.turn):
                        self.board.display_board()
                        print(f"{self.turn} is checkmated!")
                        break
                    elif self.board.stalemate(self.turn):
                        self.board.display_board()
                        print("Stalemate!")
                        break
                    #prints statement from the move and updates the board
                    color, piece = self.board.piece_info([coordinates[2],coordinates[3]])
                    from_, to_ = movesplit[:2], movesplit[2:]
                    os.system('cls')
                    print(f"{color} {piece} moved from {from_[0]}{from_[1]} to {to_[0]}{to_[1]}")
                    print("\n")
                    
            else:
                os.system('cls')
                print(messages.get(result, "Unknown error"))

            self.board.display_board()
    

if __name__ =="__main__":
    chessgame = Chess(board)
    chessgame.play()
        

