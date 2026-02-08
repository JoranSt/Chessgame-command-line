from chessPieces import *

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        back_rank = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        # white pieces
        for x in range(8):
            self.board[7][x] = back_rank[x]("white")
            self.board[6][x] = Pawn("white")

        # black pieces
        for x in range(8):
            self.board[1][x] = Pawn("black")
            self.board[0][x] = back_rank[x]("black")

    def move_piece(self,position,new_position):
        pass

    def valid_moves_for(self, position):
        piece = self.board[position[0]][position[1]]
        if piece is None:
            return []
        return piece.valid_moves(self.board, position)
    
    def display_board(self):
        print(end="  ")
        #print 1 to 9 
        for x in range(1,9):
            print(x, end="  ")
        print()

        #Print A to H on board starting with A
        unicode =65
        for row in self.board:
            print(chr(unicode), end=" ")
            unicode+=1
            #printing the board
            for xy in row:
                if xy == None:
                    print(".", end = '  ')
                else:
                    print( xy.symbol, end = '  ')
            print()
if __name__ == "__main__":
    test = Board()
    test.display_board()
    print(test.valid_moves_for((6,6)))