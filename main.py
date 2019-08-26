import game
import pawn
import bishop
import knight
import queen
import rook
import king



game=game.Game()


#team white
<<<<<<< HEAD
Wpawn1=pawn.Pawn('H2','black',game)
Wpawn2=pawn.Pawn('G2','black',game)
Wpawn3=pawn.Pawn('F2','black',game)
Wpawn4=pawn.Pawn('E2','black',game)
Wpawn5=pawn.Pawn('D2','black',game)
Wpawn6=pawn.Pawn('C2','black',game)
Wpawn7=pawn.Pawn('B2','black',game)
Wpawn8=pawn.Pawn('A2','black',game)

Wknight1=knight.Knight("B1","black",game)
Wknight2=knight.Knight("G1","black",game)

Wbishop1=bishop.Bishop("F1","black",game)
Wbishop2=bishop.Bishop("C1","black",game)

Wrook1=rook.Rook("H1","black",game)
Wrook2=rook.Rook("A1","black",game)

Wking=king.King("D1","black",game)

Wqueen=queen.Queen("E1","black",game)


#team black
Bpawn1=pawn.Pawn('H7','white',game)
Bpawn2=pawn.Pawn('G7','white',game)
Bpawn3=pawn.Pawn('F7','white',game)
Bpawn4=pawn.Pawn('E7','white',game)
Bpawn5=pawn.Pawn('D7','white',game)
Bpawn6=pawn.Pawn('C7','white',game)
Bpawn7=pawn.Pawn('B7','white',game)
Bpawn8=pawn.Pawn('A7','white',game)

Bknight1=knight.Knight("G8","white",game)
Bknight2=knight.Knight("B8","white",game)

Bbishop1=bishop.Bishop("F8","white",game)
Bbishop2=bishop.Bishop("C8","white",game)

Brook1=rook.Rook("H8","white",game)
Brook2=rook.Rook("A8","white",game)

Bking=king.King("D8","white",game)

Bqueen=queen.Queen("E8","white",game)

=======
Wpawn1=pawn.Pawn('H7','white',game)
Wpawn2=pawn.Pawn('G7','white',game)
Wpawn3=pawn.Pawn('F7','white',game)
Wpawn4=pawn.Pawn('E7','white',game)
Wpawn5=pawn.Pawn('D7','white',game)
Wpawn6=pawn.Pawn('C7','white',game)
Wpawn7=pawn.Pawn('B7','white',game)
Wpawn8=pawn.Pawn('A7','white',game)

Wknight1=knight.Knight("G8","white",game)
Wknight2=knight.Knight("B8","white",game)

Wbishop1=bishop.Bishop("F8","white",game)
Wbishop2=bishop.Bishop("C8","white",game)

Wrook1=rook.Rook("H8","white",game)
Wrook2=rook.Rook("A8","white",game)

Wking=king.King("D8","white",game)

Wqueen=queen.Queen("E8","white",game)




#team black
Bpawn1=pawn.Pawn('H2','black',game)
Bpawn2=pawn.Pawn('G2','black',game)
Bpawn3=pawn.Pawn('F2','black',game)
Bpawn4=pawn.Pawn('E2','black',game)
Bpawn5=pawn.Pawn('D2','black',game)
Bpawn6=pawn.Pawn('C2','black',game)
Bpawn7=pawn.Pawn('B2','black',game)
Bpawn8=pawn.Pawn('A2','black',game)

Bknight1=knight.Knight("B1","black",game)
Bknight2=knight.Knight("G1","black",game)

Bbishop1=bishop.Bishop("F1","black",game)
Bbishop2=bishop.Bishop("C1","black",game)

Brook1=rook.Rook("H1","black",game)
Brook2=rook.Rook("A1","black",game)

Bking=king.King("D1","black",game)

Bqueen=queen.Queen("E1","black",game)
>>>>>>> 26e8a16e9c5577fdaf6020b579d2c6343b804eec

game.play()
