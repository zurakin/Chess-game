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

        # while True:
        #     window.update()
        #     if self.winner != None:
        #         break
        #     ##white plays
        #     while True:
        #         from gui import left,right
        #         while left == None or right == None:
        #             print('sleeping')
        #             input()
        #         a = [left,right]
        #         left = None
        #         right = None
        #         if self.board[a[0]] == None or self.board[a[0]].team != 'white':
        #             print('you can only move white pieces!')
        #             continue
        #         r = self.board[a[0]].move(a[1])
        #         if r == None:
        #             break
        #         print(r)
        #
        #     window.update()
        #     if self.winner != None:
        #         break
        #
        #     ##black plays
        #     while True:
        #         from gui import left,right
        #         while left == None or right == None:
        #             input()
        #         a = [left,right]
        #         left = None
        #         right = None
        #         if self.board[a[0]] == None or self.board[a[0]].team != 'black':
        #             print('you can only move black pieces!')
        #             continue
        #         r = self.board[a[0]].move(a[1])
        #         if r == None:
        #             break
        #         print(r)

        # print("the winner is {}".format(self.winner))
        # time.sleep(5)
