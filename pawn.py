import piece

class Pawn(piece.Piece):
    def __init__(self,position,team,game):
        piece.Piece.__init__(self,position = position,team = team,game = game)
        self.type = 'pawn'
    def possible_moves(self):
        L=[]
        if self.team=="white":
            try:
                temp=self.position._get_up().position
                if game.board[temp]==None:
                    L+=[temp]
                    if self.has_moved==False:
                        temp2=self.position._get_up()._get_up().position
                        if game.board[temp2]==None:
                            L+=[temp2]
            except AssertionError :
                pass
        if self.team=="black":
            try:
                temp=self.position._get_down().position
                if game.board[temp]==None:
                    L+=[temp]
                    if self.has_moved==False:
                        temp2=self.position._get_down()._get_down().position
                        if game.board[temp2]==None:
                            L+=[temp2]
            except AssertionError :
                pass
        return L

    def possible_attacks(self):
        L=[]
        d1=None
        d2=None
        if self.team=='white':
            try:
                d1=self.position._get_diagonal_upleft()
                if d1._get_piece() != None:
                    if self.team != d1._get_piece().team :
                        L.append(d1.position)
            except AssertionError :
                pass
            try:
                d2=self.position._get_diagonal_upright()
                if d2._get_piece() != None:
                    if self.team != d2._get_piece().team :
                        L.append(d2.position)
            except AssertionError :
                pass
        elif self.team=='black':
            try:
                d1=self.position._get_diagonal_downleft()
                if d1._get_piece() != None:
                    if self.team != d1._get_piece().team :
                        L.append(d1.position)
            except AssertionError :
                pass
            try:
                d2=self.position._get_diagonal_downright()
                if d2._get_piece() != None:
                    if self.team != d2._get_piece().team :
                        L.append(d2.position)
            except AssertionError :
                pass
        return L
