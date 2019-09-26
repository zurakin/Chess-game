import position_class

class Piece:

    def __init__(self,position,team,game,initialize = True):
        self.game = game
        self.team = team
        self.status = 'Alive'
        self.has_moved = False
        self.position = position_class.Position(position,game)
        self.line = int(position[1])
        self.column = position[0]
        ## the initialize attribute is added so that when the rook class is called inside the queen class, it does't overwrite it in the board
        if initialize:
            game.board[position]  =  self
            game.pieces.append(self)

    def __repr__(self):
        return "{} {}".format(self.team,self.type)

    def get_image_path(self):
        if self.type  !=  'king' or (not self.endangered):
            return "media/{}.png".format(self.team.title()+self.type.title())
        else :
            return "media/{}Endangered.png".format(self.team.title()+self.type.title())

    def move(self,position):
        if position in self.possible_attacks():
            if self.game.board[position].type  ==  'king':
                self.game.winner = self.team
            self.game.board[self.position.position] = None
            position_class.Position(position,self.game)._get_piece().status = 'Dead'
            position_class.Position(position,self.game)._get_piece().line = None
            position_class.Position(position,self.game)._get_piece().column = None
            position_class.Position(position,self.game)._get_piece().position = None
            self.has_moved = True
            self.line = position[1]
            self.column = position[0]
            self.position = position_class.Position(position,self.game)
            self.game.board[position] = self
            if self.type  ==  'pawn' and (position[1]  ==  '1' or position[1]  ==  '8'):
                return True
            return False

        elif position in self.possible_moves():
            self.game.board[self.position.position] = None
            self.has_moved = True
            self.line = position[1]
            self.column = position[0]
            self.position = position_class.Position(position,self.game)
            self.game.board[position] = self
            return False

        else :
            return None
