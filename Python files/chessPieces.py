class Piece:
    def __init__(self, color):
        self.color = color
        self.symbol = ' '

    def valid_moves(self, board, position):
        raise NotImplementedError("Must be overriden in subclass")
    


class Pawn(Piece):
    def __init__(self, color):
        super().__init__( color)
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
            if(0<nx<8 and board[ny][nx] is not None):
                if board[ny][nx].color != self.color:
                    moves.append((ny,nx))

        return moves

      
        

    
class Rook(Piece):
    def __init__(self, color, has_moved = False):
        super().__init__(color)
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

            while 0<= ny < 8 and 0<=nx<8:
                if(board[ny][nx] == None):
                    moves.append((ny,nx))
                else:
                    if(board[ny][nx].color != self.color):
                        moves.append((ny,nx))
                    break
                ny += dy
                nx += dx
        return moves

    
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
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

            while 0<= ny < 8 and 0<=nx<8:
                if(board[ny][nx] == None):
                    moves.append((ny,nx))
                else:
                    if(board[ny][nx].color != self.color):
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
            ny, nx = y+dy, x+dx

            if 0<= ny < 8 and 0<=nx<8:
                if(board[ny][nx] == None):
                    moves.append((ny,nx))
                else:
                    if(board[ny][nx].color != self.color):
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
        for dy, dx in directions:
            ny, nx = y+dy, x+dx

            while 0<= ny < 8 and 0<=nx<8:
                if(board[ny][nx] == None):
                    moves.append((ny,nx))
                else:
                    if(board[ny][nx].color != self.color):
                        moves.append((ny,nx))
                    break
                ny += dy
                nx += dx
        return moves

class King(Piece):
    def __init__(self, color, has_moved = False):
        super().__init__(color)
        #set symbol
        if(self.color.lower() == "black"):
            self.symbol = "♔"
        else:
            self.symbol = "♚"
    def valid_moves(self, board, position):
        y, x = position
        moves = []
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        for dy, dx in directions:
            ny, nx = y+dy, x+dx

            if 0<= ny < 8 and 0<=nx<8:
                if(board[ny][nx] == None):
                    moves.append((ny,nx))
                else:
                    if(board[ny][nx].color != self.color):
                        moves.append((ny,nx))
        return moves