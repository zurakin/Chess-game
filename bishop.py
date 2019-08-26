import piece

class Bishop(piece.Piece):

    def __init__(self,position,team,game):
        piece.Piece.__init__(self,position = position,team = team,game = game)
        self.type = 'bishop'

    def possible_moves(self):
        L=[]
        temp=self.position
        while True:
            try:
                temp=temp._get_diagonal_upright()
                if temp._get_piece()!=None:
                    temp=self.position
                    break
                L+=[temp]
            except AssertionError :
                temp=self.position
                break
        while True:
            try:
                temp=temp._get_diagonal_upleft()
                if temp._get_piece()!=None:
                    temp=self.position
                    break
                L+=[temp]
            except AssertionError :
                temp=self.position
                break
        while True:
            try:
                temp=temp._get_diagonal_downleft()
                if temp._get_piece()!=None:
                    temp=self.position
                    break
                L+=[temp]
            except AssertionError :
                temp=self.position
                break
        while True:
            try:
                temp=temp._get_diagonal_downright()
                if temp._get_piece()!=None:
                    temp=self.position
                    break
                L+=[temp]
            except AssertionError :
                temp=self.position
                break
        return [i.position for i in L]



    def possible_attacks(self):
        L=[]
        temp=self.position
        while True:
            try:
                temp=temp._get_diagonal_upright()
                if temp._get_piece()==None:
                    continue
                elif temp._get_piece().team==self.team:
                    break
                else:
                    L+=[temp]
                    break
            except AssertionError :
                temp=self.position
                break
        while True:
            try:
                temp=temp._get_diagonal_upleft()
                if temp._get_piece()==None:
                    continue
                elif temp._get_piece().team==self.team:
                    break
                else:
                    L+=[temp]
                    break
            except AssertionError :
                temp=self.position
                break
        while True:
            try:
                temp=temp._get_diagonal_downright()
                if temp._get_piece()==None:
                    continue
                elif temp._get_piece().team==self.team:
                    break
                else:
                    L+=[temp]
                    break
            except AssertionError :
                temp=self.position
                break
        while True:
            try:
                temp=temp._get_diagonal_downleft()
                if temp._get_piece()==None:
                    continue
                elif temp._get_piece().team==self.team:
                    break
                else:
                    L+=[temp]
                    break
            except AssertionError :
                temp=self.position
                break
        return [i.position for i in L]
