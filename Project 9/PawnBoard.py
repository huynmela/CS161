# Author: Melanie Huynh
# Date: 27 May 2020
# Description: This program creates a 4x4 square grid with 'x' and 'o' pawns, where the objective is for each player to try and get their pieces to the opposite side.

class PawnBoard:
    def __init__(self):
        """Creates the pawns and the 4x4 board, and initializes the beginning of the game state"""
        self.__board = [['x', 'x', 'x', 'x'], ["", "", "", ""], ["", "", "", ""], ['o', 'o', 'o', 'o']]
        self.__current_state = "UNFINISHED"

    def get_current_state(self):
        """Returns the current state of the game"""
        return self.__current_state

    def check_legal(self, row_current, column_current, row_move, column_move):
        """Returns whether or not moving a piece to a desired position is a legal move. """
        legal_move = False # initializes if a move is legal

        if self.get_current_state() == "UNFINISHED":

            # Checking if movements forward or diagonal are legal for both players
            if self.__board[row_current][column_current] == 'x': # Movement check for player x
                if self.__board[row_move][column_move] == "" and row_current + 1 == row_move and column_move == column_current:
                    legal_move = True # Check in front to move
                if self.__board[row_move][column_move] == 'o':
                    if row_current + 1 == row_move and (column_current == column_move + 1 or column_current == column_move - 1):
                        legal_move = True # Check if diagonal is possible

            if self.__board[row_current][column_current] == 'o': # Movement check for player o
                if self.__board[row_move][column_move] == "" and row_current - 1  == row_move and column_move == column_current:
                    legal_move = True # Check in front to move
                if self.__board[row_move][column_move] == 'x':
                    if row_current - 1 == row_move and (column_current == column_move + 1 or column_current == column_move -1):
                        legal_move = True
        return legal_move

    def make_move(self, row_current, column_current, row_move, column_move):
        """Moves the player's piece to the desired position if it is legal and checks to see if the game is in draw."""
        if row_move > 3 or row_move < 0 or column_move > 3 or column_move < 0:
            return False # Avoid edge case in the event a desired move is outside of bounds

        if self.check_legal(row_current, column_current, row_move, column_move)  == True: # Move the piece and check if they won
            if self.__board[row_current][column_current] == 'x':
                self.__board[row_move][column_move] = 'x'
                self.__board[row_current][column_current] = ""
                return True
                if row_move == 3:
                    self.__current_state = "X_WON"
                return False

            if self.__board[row_current][column_current] == 'o': # Move the piece and check if they won
                self.__board[row_move][column_move] = 'o'
                self.__board[row_current][column_current] = ""
                return True
                if row_move == 0:
                    self.__current_state = "O_WON"
                return False

        # Check for a draw
        possible = False # mutated if a piece is able to make a move
        if self.__current_state == "UNFINISHED":
            for row in range(0, 4): # there are four rows
                for index in range(0, 4): # there are four indices in a row
                    if self.__board[row][index] == 'x': # checking for 'x' pieces
                        possible = possible or self.check_legal(row, index, row + 1, index) or self.check_legal(row, index, row + 1, index + 1) or self.check_legal(row, index, row + 1, index - 1)
                    if self.__board[row][index] == 'o': # checking for 'o' pieces
                        possible = possible or self.check_legal(row, index, row - 1, index) or self.check_legal(row, index, row - 1, index + 1) or self.check_legal(row, index, row - 1, index - 1)

            if possible == False: # if every piece is unable to move, the current state changes to a draw.
                self.__current_state = "DRAW"
        return True

