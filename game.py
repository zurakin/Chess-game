
alpha=['A','B','C','D','E','F','G','H','X']
class Game:
    def __init__(self):
        self.sheet={}
        for i in range(1,9):
            for j in alpha[:8]:
                self.sheet[j+str(i)]=None
