#!/usr/bin/env python
# encoding: utf-8

import time    

'''
This is an interactive Tic-Tac-Toe game.
The user plays as 'X' and moves first, trying to 
defeat the computer. The computer cannot be beaten here.
'''

class TicTacToe(object):
    def __init__(self):
        # board positions [1,2,3,4,5,6,7,8,9]
        # can hold 'X' or 'O' once a play is made
        self.state = [i for i in range(1,10)]
        self.turn = 'X'
        self.numTurns = 0
        self.__playGame()
        
    def __playAnotherGame(self):
        self.state = [i for i in range(1,10)]
        self.turn = 'X'
        self.numTurns = 0
        self.__playGame()
        
    def __playGame(self):
        print 'Hello, Dave.'
        time.sleep(1)
        print 'Would you like to play a game?'
        time.sleep(1)
        print 'Dave?...'
        time.sleep(1)
	
        # print empty board
        self.__printBoard()
        
        # add exception for incorrect input
        print 'In which square would you like to place an \'X\'?'
        move =  eval(raw_input('Please enter the number of the square: '))
        self.__updateBoard(move,'X')
        # checkForWin is recursive
        self.__checkForWin()
        
    def __printBoard(self):
        a = self.state
        for i in range(3):
            print '%s  |  %s  |  %s' % (a[0 + 3*i], a[1 + 3*i], a[2 + 3*i])
            if i != 2:
                print '-------------'
        print ''

    def __updateBoard(self,move,player):
        if player == 'X':
            self.state[move-1] = 'X'
            self.turn = 'O'
        elif player == 'O':
            self.state[move-1] = 'O'
            self.turn = 'X'
        self.__printBoard()
        self.numTurns += 1

    def __checkForWin(self):
        # loop over each player, see if they have won
        for c in ['O','X']:
            # rows
            if (([c,c,c] == self.state[0:3]) | 
                ([c,c,c] == self.state[3:6]) | 
                ([c,c,c] == self.state[6:10])):
                print '%s has won!' % c
                self.__endGame()
            # columns
            elif (([c,c,c] == [self.state[0 + 3*i] for i in range(3)]) | 
                  ([c,c,c] == [self.state[1 + 3*i] for i in range(3)]) | 
                  ([c,c,c] == [self.state[2 + 3*i] for i in range(3)])):
                print '%s has won!' % c
                self.__endGame()
            # diagonals
            elif (([c,c,c] == [self.state[4*i] for i in range(3)]) | 
                  ([c,c,c] == [self.state[2*i] for i in [1,2,3]])):
                print '%s has won!' % c
                self.__endGame()
        
        # if game isn't over by end of 9th move, then it's a draw
        if self.numTurns == 9:
            self.__endGame('Draw')
        # no winner yet, keep playing
        elif self.turn == 'X':
            print 'Please make another move.'
            print 'In which square would you like to place an \'X\'?'
            move =  eval(raw_input('Please enter the number of the square: '))
            self.__updateBoard(move,'X')
            self.__checkForWin()
        elif self.turn == 'O':
            # computer's turn to move
            print 'Please make another move.'
            print 'In which square would you like to place an \'O\'?'
            move =  eval(raw_input('Please enter the number of the square: '))
            self.__updateBoard(move,'O')
            self.__checkForWin()

    def __endGame(self,esult='Draw'):
        # what to do when game ends
        if result == 'Draw':
            print 'Dave...'
            print 'This game is a draw.'
        
        time.sleep(1)
        print 'Dave?...'
        print 'Would you like to play again, Dave?'
        repeat = str(raw_input('Please type \'yes\' or \'no\':'))

        if repeat == 'yes':
            self.__playAnotherGame()
        elif repeat == 'no':
            print 'Perhaps another time, Dave. Goodbye.'
            exit()
            

            

if __name__ == '__main__':

    TicTacToe()
