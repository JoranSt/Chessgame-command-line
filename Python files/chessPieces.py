class Piece:
    def __init__(self, color, checks = False):
        self.color = color
        self.symbol = ' '
        self.checks = checks

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
            #try is there because it throws an error on empty spaces, it checks if a pawn can check and appends it to the validmoves list
            try:
                if(0<nx<8 and board[ny][nx].color != self.color):
                    if(board[ny][nx].__class__.__name__ == "King"):
                        self.checks = True
                    else:
                        self.checks = False
                    moves.append((ny,nx))
            except:
                pass

        return moves

      
        

    
class Rook(Piece):
    def __init__(self, color, checks = False, has_moved = False):
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
    def __init__(self, color, checks = False):
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
    def __init__(self, color, checks = False):
        super().__init__(color)
        #set symbol
        if(self.color.lower() == "black"):
            self.symbol = "♘"
        else:
            self.symbol = "♞"

    def valid_moves(self, board, position):
        y, x = position
        moves = []
        self.checks = False
        directions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(-1,-2),(1,-2)]
        for dy, dx in directions:
            ny, nx = y+dy, x+dx

            if not (0<= ny <8 and 0<= nx <8):
                continue
            
            target = board[ny][nx]
            
            if target == None:
                moves.append((ny,nx))
                continue

            if target.color == self.color:
                continue

            if isinstance(target, King):
                self.checks = True

            moves.append((ny,nx))

        return moves




    
class Queen(Piece):
    def __init__(self, color, checks = False):
        super().__init__(color)
        #set symbol
        if (self.color.lower() == "black"):
            self.symbol = "♕"
        else:
            self.symbol = "♛"
    def valid_moves(self, board, position):
        y, x = position
        self.checks = False
        moves = []
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        #loops over all the directions
        for dy, dx in directions:
            y, x = y+dy, x+dx

            if not 0<= y <8 and 0<= x <8:
                continue
            #checks on every direction path instead of just the direction
            while 0<= y < 8 and 0<= x <8:
                target = board[y][x]

                if target == None:
                    moves.append((y,x))
                    y, x = y+dy, x+dx
                    continue

                if isinstance(target, King):
                    self.checks = True
                    break

                if target.color != self.color:
                    moves.append((y,x))
                    break
                
                else: 
                    break
        return moves
                
                    

                


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