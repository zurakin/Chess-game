import piece

class King(piece.Piece):
    def __init__(self,position,team,game):
        self.type = 'king'
        piece.Piece.__init__(self,position = position,team = team,game = game)
        self.endangered = False
        game.kings.append(self)

    def possible_moves(self):
        temp_func = [
        self.position._get_diagonal_upleft,
        self.position._get_diagonal_upright,
        self.position._get_diagonal_downleft,
        self.position._get_diagonal_downright,
        self.position._get_down,
        self.position._get_up,
        self.position._get_right,
        self.position._get_left
        ]
        L=[]

        for f in temp_func:
            try:
                L.append(f())
            except:
                pass
        L2 = []
        for p in L:
            if p._get_piece()==None:
                L2.append(p)
        return [i.position for i in L2]



    def possible_attacks(self):
        temp_func = [
        self.position._get_diagonal_upleft,
        self.position._get_diagonal_upright,
        self.position._get_diagonal_downleft,
        self.position._get_diagonal_downright,
        self.position._get_down,
        self.position._get_up,
        self.position._get_right,
        self.position._get_left
        ]
        L=[]
        for f in temp_func:
            try:
                L.append(f())
            except:
                pass
        L2 = []
        for p in L:
            if p._get_piece() != None and p._get_piece().team != self.team:
                L2.append(p)
        return [i.position for i in L2]
