import time
import random
import pygame
import bishop
import rook
import knight
import queen
import pawn
import king
import position_class

alpha = ['H','G','F','E','D','C','B','A','X']
refer = {'rook':rook.Rook,'bishop':bishop.Bishop,'knight':knight.Knight,
'queen':queen.Queen, 'pawn':pawn.Pawn ,'king':king.King }


class Game:
    def __init__(self):
        self.board = {}
        for i in range(1,9):
            for j in alpha[:8]:
                self.board[j+str(i)] = None
        self.winner = None
        self.pieces = []
        self.left = None
        self.right = None
        self.turn = 'white'
        self.turn_switch = {'white':'black','black':'white'}
        self.kings = []
        self.selec_poss = [] #this list contains the possible moves of the selected piece
        self.last_move = [] #this list contains the last made move informations so it can be undone

    def check_endangered_kings(self):
        for king in self.kings:
            king.endangered = False
            for piece in self.board.values():
                if piece  != None and king.position.position in piece.possible_attacks():
                    king.endangered = True
                    break

    def play(self,window):
        try:
            assert self.board[self.left].team  ==  self.turn
            assert self.right[0] in alpha[:-1] and int(self.right[1]) in range(1,9)
            r = self.board[self.left].move(self.right)
            assert r  !=  None
            pygame.mixer.init()
            pygame.mixer.music.load("audio/{}.wav".format(str(random.randint(1,9))))
            pygame.mixer.music.play()
            self.turn = self.turn_switch[self.turn]
            self.check_endangered_kings()
            window.update()
            for king in self.kings:
                if king.team != self.turn and king.endangered:
                    pygame.mixer.init()
                    pygame.mixer.music.load("audio/danger.wav")
                    pygame.mixer.music.play()
                    self.undo(window)
                    print('illegal move')
                    r = False
            if r :
                self.board[self.right].promote(input('what do you want to promote your piece to : '),self)
            window.update()
        except:
            print('impossible move')

    def undo(self,window):
        if len(self.last_move) == 3:
            self.board[self.last_move[1]] = self.board[self.last_move[2]]
            self.board[self.last_move[1]].has_moved = self.last_move[0]
            self.board[self.last_move[2]] = None
            self.board[self.last_move[1]].position = position_class.Position(self.last_move[1],self)
            self.turn = self.turn_switch[self.turn]
        elif len(self.last_move) == 6:
            self.board[self.last_move[1]] = self.board[self.last_move[2]]
            self.board[self.last_move[1]].has_moved = self.last_move[0]
            self.board[self.last_move[2]] = refer[self.last_move[3]](
            position = self.last_move[2],
            team = self.last_move[4],
            game = self)
            self.board[self.last_move[2]].has_moved = self.last_move[5]
            self.board[self.last_move[1]].position = position_class.Position(self.last_move[1],self)
            self.turn = self.turn_switch[self.turn]
        window.update()
