alpha=['A','B','C','D','E','F','G','H','X']


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
