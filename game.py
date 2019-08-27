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


    def play(self,window):
        try:
            assert self.board[self.left].team == self.turn
            assert self.right[0] in alpha[:-1] and int(self.right[1]) in range(1,9)
            r = self.board[self.left].move(self.right)
            window.update()
            assert r == True
            self.turn = self.turn_switch[self.turn]
        except:
            print('impossible move')
