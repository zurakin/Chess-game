import time
alpha=['H','G','F','E','D','C','B','A','X']
class Game:
    def __init__(self):
        self.board={}
        for i in range(1,9):
            for j in alpha[:8]:
                self.board[j+str(i)]=None
        self.winner = None
        self.pieces = []

    def draw(self):
        rlis= list(range(1,9))
        rlis.reverse()
        clis = ['A','B','C','D','E','F','G','H']
        for row in rlis:
            print(''.join(
            ["{}:{}".format(column+str(row),
            self.board[column+str(row)].__repr__()
            + (16-len(self.board[column+str(row)].__repr__()))*' ')
            for column in clis]))
            print('')

    def play(self,window):
        while True:
            window.update()
            if self.winner != None:
                break
            ##white plays
            while True:
                try:
                    a = input("white's turn : ").upper().split(' ')
                    if self.board[a[0]] == None or self.board[a[0]].team != 'white':
                        print('you can only move white pieces!')
                        continue
                    r = self.board[a[0]].move(a[1])
                    if r == None:
                        break
                    print(r)
                except:
                    print('error try again')

            window.update()
            if self.winner != None:
                break

            ##black plays
            while True:
                try:
                    a = input("Black's turn : ").upper().split(' ')
                    if self.board[a[0]] == None or self.board[a[0]].team != 'black':
                        print('you can only move black pieces!')
                        continue
                    r = self.board[a[0]].move(a[1])
                    if r == None:
                        break
                    print(r)
                except:
                    print('error try again')
        print("the winner is {}".format(self.winner))
        time.sleep(5)
