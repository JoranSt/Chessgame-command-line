from chessPieces import *
from copy import deepcopy
class Board:
    def __init__(self):
        #initiate board and order
        self.board = [[None for _ in range(8)] for _ in range(8)]
        back_rank = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        self.lastpiece = None
        # white pieces
        for x in range(8):
            self.board[7][x] = back_rank[x]("white")
            self.board[6][x] = Pawn("white")

        # black pieces
        for x in range(8):
            self.board[1][x] = Pawn("black")
            self.board[0][x] = back_rank[x]("black")
            
            
        

    def move_piece(self,position,new_position, turn):
        #get the position and new position and look if move is allowed
        y,x = position
        ny,nx = new_position
        piece = self.board[y][x]
        boardcopy = deepcopy(self.board) #used for simulations to see if it puts the king in check
        
        if piece is None:
            return "no_piece"
        
        if piece.color != turn:
            return "wrong_turn"
        
        moves = self.valid_moves_for(position, self.lastpiece)
        # Castling
        if isinstance(piece, King) and not piece.has_moved:
        # Kingside castling
            if nx == 6 and (y, 6) in moves:
                rook = self.board[y][7]
                if rook is None or rook.has_moved:
                    return "rook can't castle"

                # Simulate king moving through squares 5 and 6
                for i in [5, 6]:
                    boardcopy = deepcopy(self.board)
                    boardcopy[y][i] = piece
                    boardcopy[y][x] = None
                    if self.is_check(turn, boardcopy):
                        return "can't move through check"

                # Move king
                self.board[y][6] = piece
                self.board[y][x] = None
                piece.x = 6
                piece.has_moved = True

                # Move rook
                self.board[y][5] = rook
                self.board[y][7] = None
                rook.x = 5
                rook.has_moved = True

                return "ok"

            # Queenside castling
            if nx == 2 and (y, 2) in moves:
                rook = self.board[y][0]
                if rook is None or rook.has_moved:
                    return "rook can't castle"

                # Simulate king moving through squares 3 and 2
                for i in [3, 2]:
                    boardcopy = deepcopy(self.board)
                    boardcopy[y][i] = piece
                    boardcopy[y][x] = None
                    if self.is_check(turn, boardcopy):
                        return "can't move through check"

                # Move king
                self.board[y][2] = piece
                self.board[y][x] = None
                piece.x = 2
                piece.has_moved = True

                # Move rook
                self.board[y][3] = rook
                self.board[y][0] = None
                rook.x = 3
                rook.has_moved = True

                return "ok"
                
        
        if (ny,nx) in moves:
            boardcopy[ny][nx] = piece
            boardcopy[y][x] = None
            if(self.is_check(turn, boardcopy) == True):
                return "king_in_check"
            if isinstance(self.board[y][x], Pawn) and ny in (0, 7):
                OptionList = {
                    "knight": Knight, 
                    "bishop": Bishop,
                    "rook": Rook,
                    "queen": Queen
                }

                while True:
                    promotion = input("Promote pawn to (Knight, Queen, Rook, Bishop):\n")
                    promotionPiece = OptionList.get(promotion.lower())  
                    if promotionPiece is not None:
                        # Create a new piece instance
                        self.board[ny][nx] = promotionPiece(self.board[y][x].color)
                        self.board[y][x] = None
                        return "ok"
                    else:
                        print("Not a valid option. Please choose Knight, Queen, Rook, or Bishop.")
                    
            if(isinstance(piece, Pawn) and nx != x and self.board[ny][nx] is None):
                self.board[ny][nx] = piece
                self.board[y][x] = None
                self.board[y][nx] = None
                self.lastpiece = ((y,x) , (ny,nx), piece) 
                return "ok"
            
            self.board[ny][nx] = piece
            self.board[y][x] = None
            
            self.lastpiece = ((y,x) , (ny,nx), piece) 
            return "ok" 
        
        return "invalid_target"
            
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
    def valid_moves_for(self, position, lastpiece):
        piece = self.board[position[0]][position[1]]
        if piece is None:
            
            return []
        
        elif isinstance(piece, Pawn):
            
            return piece.valid_moves(self.board,position,lastpiece)
        
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
            
    def has_legal_moves(self, turn):
        for y in range(8):
            for x in range(8):
                piece = self.board[y][x]
                if(piece is not None and piece.color == turn):
                    valid_moves = self.valid_moves_for([y,x], self.lastpiece)
                    for ny,nx in valid_moves:
                        boardcopy = deepcopy(self.board) #used for simulations to see if it puts the king in check
                        boardcopy[ny][nx] = piece
                        boardcopy[y][x] = None
                        if(self.is_check(turn, boardcopy) == False):
                            print(piece.__class__.__name__ ,y,x,  ny,nx)
                            return True
                                       
        return False
                            
        

    def find_king(self, color, board=None):
        if(board == None):
            board = self.board
        for y in range(8):
            for x in range(8):
                target = board[y][x]
                if target is not None and target.color == color and isinstance(target, King):
                    return (y, x)
                
                  
    def is_check(self, color, board = None):
        if board is None:
            board = self.board
        
    
    
        #check if the king is checked
        kingsposition = self.find_king(color, board)
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
                
                target = board[ny][nx]
                if target is None:
                    ny += dy
                    nx += dx
                    continue
                
                if target.color == color:
                    break
                
                if(isinstance(target, Queen) or isinstance(target, Rook)):
                    print(f"King at {(ky,kx)} would be attacked by {target.symbol} at {(ny,nx)}")
                    return True
                    
                ny += dy
                nx += dx
                    
        #checks diagonal lines for check
        for dy,dx in diagonaldirections:
            ny, nx = ky + dy, kx + dx
            while 0<=ny<8 and 0<=nx<8:
                
                target = board[ny][nx]
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
                target = board[ny][nx]
                if isinstance(target, Knight) and target.color != color:
                    return True
                
        if color == "white":
            pawn_offsets = [(-1, -1), (-1, 1)]
        else:
            pawn_offsets = [(1, -1), (1, 1)]

        for dy, dx in pawn_offsets:
            ny, nx = ky + dy, kx + dx
            if 0 <= ny < 8 and 0 <= nx < 8:
                target = board[ny][nx]
                if isinstance(target, Pawn) and target.color != color:
                    return True   
                
        return False
            
    def checkmate(self, color):
        return  self.is_check(color) and not self.has_legal_moves(color)
    
    def stalemate(self, color):
        return not self.is_check(color) and not self.has_legal_moves(color)
                    
                       
                    
                    
         
        
                    
                

if __name__ == "__main__":
    test = Board()
    test.display_board()
    print(test.valid_moves_for((0,4)))
    color, symbol = test.piece_info((0,4))
    print(color, symbol)