import position_class

class Piece:

    def __init__(self,position,team,game):
        self.team=team
        self.status='Alive'
        self.has_moved=False
        self.position=position_class.Position(position)
        self.line=int(position[1])
        self.column=position[0]
        game.board[position]=self

    def __repr__(self):
        return "{} {}".format(self.team,self.type)

    def move(self,position):
        if position in self.possible_attacks():
            game.board[self.position.position]=None
            position_class.Position(position)._get_piece().status='Dead'
            position_class.Position(position)._get_piece().line=None
            position_class.Position(position)._get_piece().column=None
            position_class.Position(position)._get_piece().position=None
            self.has_moved=True
            self.line=position[1]
            self.column=position[0]
            self.position=position_class.Position(position)
            game.board[position]=self

        elif position in self.possible_moves():
            game.board[self.position.position]=None
            self.has_moved=True
            self.line=position[1]
            self.column=position[0]
            self.position=position_class.Position(position)
            game.board[position]=self

        else :
            print('impossible move')
