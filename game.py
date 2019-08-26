
alpha=['H','G','F','E','D','C','B','A','X']
class Game:
    def __init__(self):
        self.board={}
        for i in range(1,9):
            for j in alpha[:8]:
                self.board[j+str(i)]=None

    def draw(self):
        for row in range(1,9):
            print(''.join(
            ["{}:{}".format(column+str(row),
            self.board[column+str(row)].__repr__()
            + (16-len(self.board[column+str(row)].__repr__()))*' ')
            for column in alpha[:8]]))
            print('')
