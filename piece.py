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
