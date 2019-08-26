import piece

class Queen(piece.Piece):
    def __init__(self,position,team,game):
        piece.Piece.__init__(self,position = position,team = team,game = game)
        self.type = 'queen'

    def possible_moves(self):
        return Rook(self.position.position,self.team).possible_moves()
        +Bishop(self.position.position,self.team).possible_moves()
    def possible_attacks(self):
        return Rook(self.position.position,self.team).possible_attacks()
        +Bishop(self.position.position,self.team).possible_attacks()
