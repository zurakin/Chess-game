class Queen(Piece):
    def possible_moves(self):
        return Rook(self.position.position,self.team).possible_moves()+
        Bishop(self.position.position,self.team).possible_moves()
    def possible_attacks(self):
        return Rook(self.position.position,self.team).possible_attacks()+
        Bishop(self.position.position,self.team).possible_attacks()
