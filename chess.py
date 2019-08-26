alpha=['A','B','C','D','E','F','G','H','X']
class Game:
    def __init__(self):
        self.sheet={}
        for i in range(1,9):
            for j in alpha[:8]:
                self.sheet[j+str(i)]=None



class Position:
    def __init__(self,position):
        self.position=position
        self.line=int(position[1])
        self.column=position[0]
        assert self.line in range(1,9) and self.column in alpha
        assert self.column!='X'

    def _get_piece(self):
        return game.sheet[self.position]


    def _get_up(self):
        return Position(self.column+str(self.line-1))

    def _get_down(self):
        return Position(self.column+str(self.line+1))

    def _get_left(self):
        return Position(alpha[alpha.index(self.column)-1]+str(self.line))

    def _get_right(self):
        return Position(alpha[alpha.index(self.column)+1]+str(self.line))

    def _get_line(self):
        return [Position(alpha[i]+str(self.line)) for i in range(8)]

    def _get_column(self):
        return [Position(self.column+str(i)) for i in range(8)]

    def _get_diagonal_upleft(self):
        return Position(alpha[alpha.index(self.column)-1]+str(self.line-1))

    def _get_diagonal_upright(self):
        return Position(alpha[alpha.index(self.column)+1]+str(self.line-1))

    def _get_diagonal_downright(self):
        return Position(alpha[alpha.index(self.column)+1]+str(self.line+1))

    def _get_diagonal_downleft(self):
        return Position(alpha[alpha.index(self.column)-1]+str(self.line+1))

class Piece:

    def __init__(self,position,team):
        self.team=team
        self.status='Alive'
        self.has_moved=False
        self.position=Position(position)
        self.line=int(position[1])
        self.column=position[0]
        game.sheet[position]=self

    def move(self,position):
        if position in self.possible_attacks():
            game.sheet[self.position.position]=None
            Position(position)._get_piece().status='Dead'
            Position(position)._get_piece().line=None
            Position(position)._get_piece().column=None
            Position(position)._get_piece().position=None
            self.has_moved=True
            self.line=position[1]
            self.column=position[0]
            self.position=Position(position)
            game.sheet[position]=self

        elif position in self.possible_moves():
            game.sheet[self.position.position]=None
            self.has_moved=True
            self.line=position[1]
            self.column=position[0]
            self.position=Position(position)
            game.sheet[position]=self

        else :
            print('impossible move')



class Pawn(Piece):
    def possible_moves(self):
        L=[]
        if self.team=="white":
            try:
                temp=self.position._get_up().position
                if game.sheet[temp]==None:
                    L+=[temp]
                    if self.has_moved==False:
                        temp2=self.position._get_up()._get_up().position
                        if game.sheet[temp2]==None:
                            L+=[temp2]
            except AssertionError :
                pass
        if self.team=="black":
            try:
                temp=self.position._get_down().position
                if game.sheet[temp]==None:
                    L+=[temp]
                    if self.has_moved==False:
                        temp2=self.position._get_down()._get_down().position
                        if game.sheet[temp2]==None:
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



class King(Piece):
    def possible_moves(self):
        L=[]
        try :
            L+=[self.position._get_diagonal_upleft()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_diagonal_upright()]
        except AssertionError  :
            pass
        try:
            L+=[self.position._get_diagonal_downleft()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_diagonal_downright()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_down()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_up()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_right()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_left()]
        except AssertionError :
            pass
        for p in L:
            if p._get_piece()!=None:
                L.remove(p)
        return [i.position for i in L]
    def possible_attacks(self):
        L=[]
        try :
            L+=[self.position._get_diagonal_upleft()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_diagonal_upright()]
        except AssertionError  :
            pass
        try:
            L+=[self.position._get_diagonal_downleft()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_diagonal_downright()]
        except AssertionError :
            pass
        try:
            L+=[self._get_up(),self._get_down()]
        except AssertionError :
            pass
        try:
            L+=[self._get_right()]
        except AssertionError :
            pass
        try:
            L+=[self._get_left()]
        except AssertionError :
            pass
        for p in L:
            if p._get_piece()==None or p._get_piece().team==self.team:
                L.remove(p)
        return [i.position for i in L]

class Bishop(Piece):
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


class Rook(Piece):
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

class Queen(Piece):
    def possible_moves(self):
        return Rook(self.position.position,self.team).possible_moves()+Bishop(self.position.position,self.team).possible_moves()
    def possible_attacks(self):
        return Rook(self.position.position,self.team).possible_attacks()+Bishop(self.position.position,self.team).possible_attacks()

class Knight(Piece):
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









game=Game()


#team white
Wpawn1=Pawn('A7','white')
Wpawn2=Pawn('B7','white')
Wpawn3=Pawn('C7','white')
Wpawn4=Pawn('D7','white')
Wpawn5=Pawn('E7','white')
Wpawn6=Pawn('F7','white')
Wpawn7=Pawn('G7','white')
Wpawn8=Pawn('H7','white')

Wknight1=Knight("B8","white")
Wknight2=Knight("G8","white")

Wbishop1=Bishop("C8","white")
Wbishop2=Bishop("F8","white")

Wrook1=Rook("A8","white")
Wrook2=Rook("H8","white")

Wking=King("E8","white")

Wqueen=Queen("D8","white")




#team black
Bpawn1=Pawn('A2','black')
Bpawn2=Pawn('B2','black')
Bpawn3=Pawn('C2','black')
Bpawn4=Pawn('D2','black')
Bpawn5=Pawn('E2','black')
Bpawn6=Pawn('F2','black')
Bpawn7=Pawn('G2','black')
Bpawn8=Pawn('H2','black')

Bknight1=Knight("B1","black")
Bknight2=Knight("G1","black")

Bbishop1=Bishop("C1","black")
Bbishop2=Bishop("F1","black")

Brook1=Rook("A1","black")
Brook2=Rook("H1","black")

Bking=King("E1","black")

Bqueen=Queen("D1","black")
