import sys
import turtle  
import numpy as np
from enum import Enum

# Switch Function for determining gamestate
def switch(GameState):
    if GameState == "setup":
        return "setup"
    elif GameState == "PlayerTurn":
        return "PlayerTurn"
    elif GameState == "GameOver":
        return "GameOver"
   

# First, intialize gameloop
while True: 
    # Second, create gameboard screen  
    screen_1 = turtle.Screen()  
    screen_1.title("Battleship")  
    screen_1.bgcolor("lightblue")  
    screen_1.setup(width = 1050, height = 650)    
     
    print(switch("setup")) 
    # Based on Gamestate:
    # ___________________

    # 1. Setup
    # Initialize Both Players
    # Need to create a player class for
    # to create a player class for holding gamepices in the current location and rotation
    # Allow  users to Pick Pieces
    # now allow players to pick pices and do a drag-and-drop    

    # 2. PlayerTurn
    # Start Switch Player Timer
    # Start round timer when switch player time ends
    # Switch Player on round timer end

    # 3. GameOver
    # End game on no ships left for either or player


    # board = [
    #         [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '], 
    #         [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '] , 
    #         [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],
    #         [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],
    #         [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],
    #         [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],
    #         [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],
    #         [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],
    #         [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],
    #         [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' '],
    #         [' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ',' ']
    #     ]
    # print(board)