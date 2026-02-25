class Piece:
    def __init__(self, color):
        self.color = color
        self.symbol = ' '

    def valid_moves(self, board, position):
        raise NotImplementedError("Must be overriden in subclass")
    


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        #set symbol
        if(self.color.lower() == "black"):
            self.symbol = '♙'
        else:
            self.symbol = '♟'
        
    #if on backrank promote
    def valid_moves(self, board, position):
        y,x = position
        moves = []
        direction = -1 if self.color == "white" else 1
        start_row = 6 if self.color.lower() == "white" else 1

        # one square forward
        ny = y + direction
        if 0 <= ny < 8 and board[ny][x] is None:
            moves.append((ny, x))

            # two squares forward (only if first move is possible)
            if y == start_row and board[y + 2*direction][x] is None:
                moves.append((y + 2*direction, x))
        for nx in [x-1,x+1]:
            #try is there because it throws an error on empty spaces, it checks if a pawn can capture a piece and appends it to the validmoves list
            
         
            if 0 <= nx < 8:
                target = board[ny][nx]
                if target is not None and target.color != self.color:
                    moves.append((ny, nx))

        return moves

      
        

    
class Rook(Piece):
    def __init__(self, color, has_moved = False):
        super().__init__(color)
        self.has_moved = has_moved
        #set symbol
        if(self.color.lower() == "black"):
            self.symbol = '♖'
        else:
            self.symbol = '♜'
            
    def valid_moves(self,board,position):
        y, x = position
        moves = []
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for dy, dx in directions:
            
            ny, nx = y+dy, x+dx
            
            #loops over while inside the board range and stops when it hits a piece
            while 0<= ny < 8 and 0<=nx<8:
                target = board[ny][nx]
                if(target == None):
                    moves.append((ny,nx))
                else:
                    #checks if its a capturable piece
                    if(target.color != self.color):
                        moves.append((ny,nx))
                    break
                ny += dy
                nx += dx
        return moves

    
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.checks = False
        #set symbol
        if(self.color.lower() == "black"):
            self.symbol = "♗"
        else:
            self.symbol = '♝'


    def valid_moves(self, board, position):
        y, x = position
        moves = []
        directions = [(1,1),(-1,-1),(-1,1),(1,-1)]
        for dy, dx in directions:
            ny, nx = y+dy, x+dx
            #loops over while inside the board range and stops when it hits a piece
            while 0<= ny < 8 and 0<=nx<8:
                target = board[ny][nx]
                if(target == None):
                    moves.append((ny,nx))
                else:
                    if(target.color != self.color):
                        moves.append((ny,nx))
                    break
                ny += dy
                nx += dx
        return moves

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        #set symbol
        if(self.color.lower() == "black"):
            self.symbol = "♘"
        else:
            self.symbol = "♞"

    def valid_moves(self, board, position):
        y, x = position
        moves = []
        directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(-1,-2),(1,-2)]
        for dy, dx in directions:
            #checks if the move is legal on all directions
            ny, nx = y+dy, x+dx

            if (0<= ny <8 and 0<= nx <8):
                
                target = board[ny][nx]
                
                if target == None or target.color != self.color:
                    moves.append((ny,nx))

        return moves




    
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        
        #set symbol
        if (self.color.lower() == "black"):
            self.symbol = "♕"
        else:
            self.symbol = "♛"
    def valid_moves(self, board, position):
        y, x = position
        moves = []
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        #loops over all the directions
        for dy, dx in directions:
            ny, nx = y+dy, x+dx

            if not (0<= ny <8 and 0<= nx <8):
                continue
            #checks for legal moves on every direction path instead of just the direction and stops at a piece
            while 0<= ny < 8 and 0<= nx <8:
                target = board[ny][nx]

                if target == None:
                    moves.append((ny,nx))
                    ny, nx = ny+dy, nx+dx
                    continue
                
                if target.color == self.color:
                    break
                
                moves.append((ny,nx)) 
                break
        return moves
                
                    

class King(Piece):
    def __init__(self, color, has_moved = False):
        super().__init__(color)
        #set symbol
        self.has_moved = has_moved
        if(self.color.lower() == "black"):
            self.symbol = "♔"
        else:
            self.symbol = "♚"
    def valid_moves(self, board, position):
        y, x = position
        moves = []
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        if(self.has_moved == False):
            if board[y][1] is None and board[y][2] is None and board[y][3] is None:
                rook = board[y][0]
                if rook and not rook.has_moved:
                    moves.append((y, 2))

            # Kingside castling (king moves to column 6)
            if board[y][5] is None and board[y][6] is None:
                rook = board[y][7]
                if rook and not rook.has_moved:
                    moves.append((y, 6))
                
                
                
        for dy, dx in directions:
            #checks for valid moves it doesnt check for checks right now because those are stored within the pieces.
            ny, nx = y+dy, x+dx
            
            

            if 0<= ny < 8 and 0<=nx<8:
                target = board[ny][nx]
                if(target == None or target.color != self.color):
                    moves.append((ny,nx))
        
        return moves