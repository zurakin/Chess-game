import time

alpha = ['H','G','F','E','D','C','B','A','X']



class Game:
    def __init__(self):
        self.board={}
        for i in range(1,9):
            for j in alpha[:8]:
                self.board[j+str(i)]=None
        self.winner = None
        self.pieces = []
        self.left = None
        self.right = None
        self.turn = 'white'
        self.turn_switch = {'white':'black','black':'white'}
        self.kings = []
        self.selec_poss = [] #this list contains the possible moves of the selected piece

    def check_endangered_kings(self):
        for king in self.kings:
            king.endangered = False
            for piece in self.board.values():
                if piece !=None and king.position.position in piece.possible_attacks():
                    king.endangered = True
                    break

    def play(self,window):
        # try:
        assert self.board[self.left].team == self.turn
        assert self.right[0] in alpha[:-1] and int(self.right[1]) in range(1,9)
        r = self.board[self.left].move(self.right)
        assert r != False
        self.turn = self.turn_switch[self.turn]
        self.check_endangered_kings()
        if r != True:
            pawn = self.board[self.right]
            pawn.promote(input('what do you want to promote your piece to : '),self)
        window.update()
        # except:
        #     print('impossible move')
