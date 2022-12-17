# Input
# Output
# Compare Two Values
# Perform Math
# Store Data

import numpy as np
from enum import Enum

true = True
false = False


def is_valid_position(pos:'Vector2') -> bool:
    return (pos.x > -1 and pos.x < 11 and pos.y > -1 and pos.y < 11) 

# Battleship!
class Board:
    class Type(Enum):
        GUESS=0 #CONTAINS PLAYERS GUESSES
        PIECE=1 # cONTAINS PIECES

    def __init__(self, player, type: 'Board.Type'):        
        self.board = None
        self.reset_board()
        self.player = player
        self.type = type

    def reset_board(self): # Purpose? To
        self.board = [
            [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '], [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '] , [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],[' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],[' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],[' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],[' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],[' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],[' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],[' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],[' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ']
        ]
    
    def update(self):
        self.reset_board()
        if self.type == Board.Type.GUESS: # Set of Vectors
            for guess, value in self.player.guesses:
                self.board[guess.x][guess.y] = value
        else: # List of Pieces -> Coordinates
            for piece in self.player.pieces:
                for i, coord in  enumerate(piece.coords):
                    self.board[coord.x][coord.y] = piece.body[i]

    def print_state(self):
        print("-"*15)
        for row in self.board:
            print('|{}|'.format(row))
        print("-"*15)
    
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return ( (self.x - other.x)**2 + (self.y - other.y)**2 )**.5
    
    def equals(self, other):
        return (self.x==other.x) and (self.y==other.y)


class GamePiece:
    class Type(Enum):
        DESTROYER = 0
        SUBMARINE = 1
        CRUISER = 2
        BATTLESHIP =3
        CARRIER = 4
    PIECE_SIZE = {
        Type.DESTROYER: 2,
        Type.SUBMARINE: 3,
        Type.CRUISER: 3,
        Type.BATTLESHIP: 4,
        Type.CARRIER: 5
    }

    def __init__(self, type:Type, position:Vector2, rotation:int):
        self.type = type
        self.position = position
        self.rotation = rotation
        self.body = np.full(shape=(GamePiece.PIECE_SIZE[self.type]), fill_value='O')
        # print(self.body)
        # Generate a list of Vectors that contain the ship
        self.coords = np.full(shape=(GamePiece.PIECE_SIZE[self.type]), fill_value=Vector2(-1,-1))
        if self.rotation == 0:
            for i in range(GamePiece.PIECE_SIZE[self.type]):
                self.coords[i] = Vector2(self.position.x, self.position.y + i)
    
        elif self.rotation == 1:
            for i in range(GamePiece.PIECE_SIZE[self.type]):
                self.coords[i] = Vector2(self.position.x + i, self.position.y + i)
        
        elif self.rotation == -1:
            for i in range(GamePiece.PIECE_SIZE[self.type]):
                self.coords[i] = Vector2(self.position.x - i, self.position.y + i)
        
        elif self.rotation == 2:
            for i in range(GamePiece.PIECE_SIZE[self.type]):
                self.coords[i] = Vector2(self.position.x + i, self.position.y)
                
        print('Created a Gamepiece')                

class Player:
    def __init__(self):
        self.guesses= {} # Set of Vectors  
        self.pieces=[] # Lists of lists of Vectors
        self.guess_board = Board(self,Board.Type.GUESS)
        self.piece_board = Board(self, Board.Type.PIECE)
    def hit_query(self, guess:Vector2):
        # Find origin pos, and all containing positions, and figure out if that matches the location: 
        hit = -1
        for piece in self.pieces:
            if piece.position.dist(guess) > GamePiece.PIECE_SIZE[piece.type]:
                continue # Miss
            for i, pos in enumerate(piece.coords):
                if guess.equals(pos):
                    hit = 1
                    piece.body[i] = 'X'
                    self.piece_board.update()
                    break
        return hit    
    
    def make_query(self, guess:Vector2, other:'Player'):
        query = other.hit_query(guess)
        self.guesses.append((guess, 'X')) if query == 1 else self.guesses.append((guess, 'U')) 

    
    def add_piece(self, piece:GamePiece):
        for p in self.pieces: # Query each piece to ensure no overlaps.
            for pos in p.coords:
                for pos_new in piece.coords:
                    if pos_new.equals(pos):
                        return -1 # Conflict
        for pos in piece.coords:
            if not is_valid_position(pos):
                return -2 # invalid postion
        self.pieces.append(piece)  
        self.piece_board.update()    
        return 0 # Success



'''
Features Done:
- Piece Generation
- Player Creation, has a piece board, guess board, a way to deal with other quesses, 
- Board Representation of the state in the game. 

Features to be Implemented:
Game Loop- 
    Two Players: Initialization Phase, Game Phase which implies and ending phase
    1. Initialization Phase
        - Set Up both players Piece Boards:
    2. Game Phase
    3. End Phase



'''










#note: she learned about input validation, escape sequences, AND OR and NOT validation
#probably could simplify the print statements with new line escape sequences 
#so she can learn about putting less codes and save clock cycles
#
#for the rotation of the ship i'm thinking read the first two digits of the string 
#which should be 01 to 11, then the last digit should be A to K
#then convert the letter part to the equivalent number to be passed into the GamePiece class

#some of her variables are named different but the logic of the code is the same