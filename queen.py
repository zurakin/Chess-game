import piece
import bishop
import rook

class Queen(piece.Piece):
    def __init__(self,position,team,game):
        self.type = 'queen'
        piece.Piece.__init__(self,position = position,team = team,game = game)

    def possible_moves(self):
        return rook.Rook(self.position.position,self.team,self.game, initialize = False).possible_moves()+bishop.Bishop(self.position.position,self.team,self.game, initialize = False).possible_moves()

    def possible_attacks(self):
        return rook.Rook(self.position.position,self.team,self.game, initialize = False).possible_attacks()+bishop.Bishop(self.position.position,self.team,self.game, initialize = False).possible_attacks()
