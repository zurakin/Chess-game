import game
import pawn
import bishop
import knight
import queen
import rook
import king
import gui

alpha = ['H','G','F','E','D','C','B','A','X']
alpha2 = ['A','B','C','D','E','F','G','H']
game = game.Game()


#team white
Wpawn1=pawn.Pawn('H2','white',game)
Wpawn2=pawn.Pawn('G2','white',game)
Wpawn3=pawn.Pawn('F2','white',game)
Wpawn4=pawn.Pawn('E2','white',game)
Wpawn5=pawn.Pawn('D2','white',game)
Wpawn6=pawn.Pawn('C2','white',game)
Wpawn7=pawn.Pawn('B2','white',game)
Wpawn8=pawn.Pawn('A2','white',game)


Wknight1=knight.Knight("B1","white",game)
Wknight2=knight.Knight("G1","white",game)


Wbishop1=bishop.Bishop("F1","white",game)
Wbishop2=bishop.Bishop("C1","white",game)

Wrook1=rook.Rook("H1","white",game)
Wrook2=rook.Rook("A1","white",game)

Wking=king.King("D1","white",game)

Wqueen=queen.Queen("E1","white",game)


#team black
Bpawn1=pawn.Pawn('H7','black',game)
Bpawn2=pawn.Pawn('G7','black',game)
Bpawn3=pawn.Pawn('F7','black',game)
Bpawn4=pawn.Pawn('E7','black',game)
Bpawn5=pawn.Pawn('D7','black',game)
Bpawn6=pawn.Pawn('C7','black',game)
Bpawn7=pawn.Pawn('B7','black',game)
Bpawn8=pawn.Pawn('A7','black',game)

Bknight1=knight.Knight("G8","black",game)
Bknight2=knight.Knight("B8","black",game)

Bbishop1=bishop.Bishop("F8","black",game)
Bbishop2=bishop.Bishop("C8","black",game)

Brook1=rook.Rook("H8","black",game)
Brook2=rook.Rook("A8","black",game)

Bking=king.King("D8","black",game)

Bqueen=queen.Queen("E8","black",game)



def lgetxy(event):
    try:
        game.left = alpha2[int(event.x/80)-1]+str(9-int(event.y/80))
    except:
        print('error')

def rgetxy(event):
    try:
        game.right = alpha2[int(event.x/80)-1]+str(9-int(event.y/80))
    except:
        print('error')
    game.play(guiw)



guiw = gui.Window(game)
guiw.canvas.bind('<Button-1>', lgetxy)
guiw.canvas.bind('<Button-3>', rgetxy)
guiw.canvas.grid()
guiw.update()
# game.play(window = guiw)
guiw.window.mainloop()
