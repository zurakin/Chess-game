import time
alpha=['H','G','F','E','D','C','B','A','X']
class Game:
    def __init__(self):
        self.kings = []
        self.board={}
        for i in range(1,9):
            for j in alpha[:8]:
                self.board[j+str(i)]=None
        self.winner = None

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

    def play(self):
        while True:
            if self.kings[0].status == 'Dead':
                self.winner = 'black'
                break
            ##white plays
            while True:
                self.draw()
                a = input("white's turn : ").upper().split(' ')
                if self.board[a[0]] == None or self.board[a[0]].team != 'white':
                    print('you can only move white pieces!')
                    continue
                r = self.board[a[0]].move(a[1])
                if r == None:
                    break
                print(r)

            if self.kings[1].status == 'Dead':
                self.winner = 'white'
                break

            ##black plays
            while True:
                self.draw()
                a = input("Black's turn : ").upper().split(' ')
                if self.board[a[0]] == None or self.board[a[0]].team != 'black':
                    print('you can only move black pieces!')
                    continue
                r = self.board[a[0]].move(a[1])
                if r == None:
                    break
                print(r)
        print("the winner is {}".format(self.winner))
        time.sleep(5)
