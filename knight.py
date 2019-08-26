import piece

class Knight(piece.Piece):
    def __init__(self,position,team,game):
        piece.Piece.__init__(self,position = position,team = team,game = game)
        self.type = 'knight'
    def allpos(self):
        P=[]
        try:
            P.append(self.position._get_up()._get_up()._get_right())
        except AssertionError :
            pass
        try:
            P.append(self.position._get_up()._get_up()._get_left())
        except AssertionError :
            pass
        try:
            P.append(self.position._get_right()._get_right()._get_up())
        except AssertionError :
            pass
        try:
            P.append(self.position._get_right()._get_right()._get_down())
        except AssertionError :
            pass
        try:
            P.append(self.position._get_left()._get_left()._get_up())
        except AssertionError :
            pass
        try:
            P.append(self.position._get_left()._get_left()._get_down())
        except AssertionError :
            pass
        try:
            P.append(self.position._get_down()._get_down()._get_right())
        except AssertionError :
            pass
        try:
            P.append(self.position._get_down()._get_down()._get_left())
        except AssertionError :
            pass
        return L

    def possible_moves(self):
        L=self.allpos()
        for p in P:
            if p._get_piece() == None:
                L.append(p.position)
        return L

    def possible_attacks(self):
        L=self.allpos()
        for p in P:
            if p._get_piece() != None:
                if p._get_piece().team!=self.team:
                    L.append(p.position)
        return L
