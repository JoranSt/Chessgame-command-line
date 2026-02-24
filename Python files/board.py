from chessPieces import *
import os 
class Board:
    def __init__(self):
        #initiate board and order
        self.board = [[None for _ in range(8)] for _ in range(8)]
        back_rank = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        # white pieces
        for x in range(8):
            self.board[7][x] = back_rank[x]("white")
           # self.board[6][x] = Pawn("white")

        # black pieces
        for x in range(8):
            #self.board[1][x] = Pawn("black")
            self.board[0][x] = back_rank[x]("black")
        

    def move_piece(self,position,new_position, turn):
        #get the position and new position and look if move is allowed
        y,x = position
        ny,nx = new_position
        piece = self.board[y][x]
        if piece is None or piece.color != turn:
            return False
        else:
            moves = piece.valid_moves(self.board, position)
            if (ny,nx) in moves:
                self.board[ny][nx] = piece
                self.board[y][x] = None
                piece.valid_moves(self.board,new_position)
                return True 
            else:
                return False
            
    @staticmethod
    def unicode_to_index(symbols):
        #changes the input from strings to coordinates using unicode
        coordinates = []
        for x in symbols:
            try:
                coordinates.append(int(x)-1)
            except:
                coordinates.append(ord(x.upper()) - 65)
        return coordinates
                                      
    
    #for test purposes
    def piece_info(self, position):
        piece = self.board[position[0]][position[1]]
        if piece is None:
            return None, None
        return piece.color, piece.__class__.__name__
    
    #passes variables to the chesspieces to check for validmoves
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

    def find_king(self, color):
        for y in range(8):
            for x in range(8):
                target = self.board[y][x]
                if target is not None and target.color == color and isinstance(target, King):
                    return (y, x)
                
                  
    def is_check(self, color):
        #check if the king is checked
        kingsposition = self.find_king(color)
        if kingsposition is None:
            raise ValueError(f"No {color} king found on the board!")
                    
                    
        straightdirections = [(1,0),(-1,0),(0,1),(0,-1)]
        diagonaldirections = [(1,1),(-1,-1),(-1,1),(1,-1)]
        knightdirections = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(-1,-2),(1,-2)]
        ky, kx = kingsposition
        #checks every line direction for attack
        for dy,dx in straightdirections:
            ny, nx = ky + dy, kx + dx
            while 0<=ny<8 and 0<=nx<8:
                
                target = self.board[ny][nx]
                if target is None:
                    ny += dy
                    nx += dx
                    continue
                
                if target.color == color:
                    break
                
                if(isinstance(target, Queen) or isinstance(target, Rook)):
                    return True
                    
                ny += dy
                nx += dx
                    
        #checks diagonal lines for check
        for dy,dx in diagonaldirections:
            ny, nx = ky + dy, kx + dx
            while 0<=ny<8 and 0<=nx<8:
                
                target = self.board[ny][nx]
                if target is None:
                    ny += dy
                    nx += dx
                    continue
                
                if target.color == color:
                    break
                
                if(isinstance(target, Queen) or isinstance(target, Bishop)):
                    return True
                    
                ny += dy
                nx += dx
                
        #checks if knights are putting the king in check
        for dy, dx in knightdirections:
            ny, nx = ky+dy, kx+dx
            
            if (0 <= ny <8 and 0 <= nx <8):
                target = self.board[ny][nx]
                if isinstance(target, Knight) and target.color != color:
                    return True
                
        if color == "white":
            pawn_offsets = [(-1, -1), (-1, 1)]
        else:
            pawn_offsets = [(1, -1), (1, 1)]

        for dy, dx in pawn_offsets:
            ny, nx = ky + dy, kx + dx
            if 0 <= ny < 8 and 0 <= nx < 8:
                target = self.board[ny][nx]
                if isinstance(target, Pawn) and target.color != color:
                    return True   
                
        return False
            
                    
                    
                    
         
        
                    
                

if __name__ == "__main__":
    test = Board()
    test.display_board()
    print(test.valid_moves_for((0,4)))
    color, symbol = test.piece_info((0,4))
    print(color, symbol)