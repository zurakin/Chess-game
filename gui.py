from tkinter import *
from PIL import ImageTk



alpha = ['A','B','C','D','E','F','G','H']

def convert(position):
    return ((alpha.index(position[0])+1)*80 ,(9-int(position[1]))*80 )



class Window():
    def __init__(self,game):
        ##create a window and a canvas
        self.game = game
        self.window = Tk()
        self.window.title('Golden duel Chess')
        self.window.iconbitmap(r"media\icon.ico")
        self.canvas = Canvas(self.window, width = 800, height = 800, bg = 'brown')
        ##draw the background
        self.background = ImageTk.PhotoImage(file = r"media\board_resized2.png")
        self.background_seen = self.canvas.create_image(0,0,image = self.background ,anchor = NW)
        ##add an image for the selec_poss
        self.selec_poss_im = ImageTk.PhotoImage(file = r"media\selec_poss.png")
        self.selec_poss_seen = []

    def update(self):
        for piece in self.game.pieces:
            if piece.status  == 'Dead':
                self.canvas.delete(piece.seen_image)
            else:
                piece.image = ImageTk.PhotoImage(file = piece.get_image_path())
                piece.seen_image = self.canvas.create_image(
                convert(piece.position.position)[0],
                convert(piece.position.position)[1],
                image = piece.image ,
                anchor = NW
                )
        self.window.update()
