import piece

class Rook(piece.Piece):

    def __init__(self,position,team,game):
        piece.Piece.__init__(self,position = position,team = team,game = game)
        self.type = 'rook'

    def possible_moves(self):
        L=[]
        temp=self.position
        while True:
            try:
                temp=temp._get_up()
                if temp._get_piece()!=None:
                    temp=self.position
                    break
                L+=[temp]
            except AssertionError :
                temp=self.position
                break

        while True:
            try:
                temp=temp._get_down()
                if temp._get_piece()!=None:
                    temp=self.position
                    break
                L+=[temp]
            except AssertionError :
                temp=self.position
                break

        while True:
            try:
                temp=temp._get_right()
                if temp._get_piece()!=None:
                    temp=self.position
                    break
                L+=[temp]
            except AssertionError :
                temp=self.position
                break

        while True:
            try:
                temp=temp._get_left()
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
                temp=temp._get_right()
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
                temp=temp._get_left()
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
                temp=temp._get_down()
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
                temp=temp._get_up()
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