class Piece:
    def __init__(self, color):
        self.color = color
        self.symbol = ' '

    def valid_moves(self, board, position):
        raise NotImplementedError("Must be overriden in subclass")
    


class Pawn(Piece):
    def __init__(self, color, has_moved = False):
        super().__init__( color)
        #set symbol
        if(self.color.lower() == "white"):
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

        return moves

      
        

    
    def can_take(self, board, position, take_position):
        pass
    
class Rook(Piece):
    def __init__(self, color, has_moved = False):
        super().__init__(color)
        #set symbol
        if(self.color.lower() == "white"):
            self.symbol = '♖'
        else:
            self.symbol = '♜'
            
    def valid_moves(self,board,position):
        return super().valid_moves(board,position)
    
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        #set symbol
        if(self.color.lower() == "white"):
            self.symbol = "♗"
        else:
            self.symbol = '♝'
    def valid_moves(self, board, position):
        return super().valid_moves(board, position)

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        #set symbol
        if(self.color.lower() == "white"):
            self.symbol = "♘"
        else:
            self.symbol = "♞"

    def valid_moves(self, board, position):
        return super().valid_moves(board, position)
    
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        #set symbol
        if (self.color.lower() == "white"):
            self.symbol = "♕"
        else:
            self.symbol = "♛"
    def valid_moves(self, board, position):
        return super().valid_moves(board, position)

class King(Piece):
    def __init__(self, color, has_moved = False):
        super().__init__(color)
        #set symbol
        if(self.color.lower() == "white"):
            self.symbol = "♔"
        else:
            self.symbol = "♚"
    def valid_moves(self, board, position):
        return super().valid_moves(board, position)