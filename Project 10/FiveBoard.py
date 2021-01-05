# Author: Melanie Huynh
# Date: 3 June 2020
# Description: This program is a 5x5 tic-tac-toe game for two players. The objective of the game is for each play to try and get 5 in a row.

class FiveBoard:
    def __init__(self):
        """Creates the 15x15 board and initializes the beginning of the game state."""
        self._board = []
        for i in range(15):
            self._board.append(["" for i in range(15)]) # creates the 15x15 board
        self._current_state = "UNFINISHED" # initializes the state as unfinished
    def get_current_state(self):
        """Returns the current state of the game."""
        return self._current_state

    def print(self):
        for item in self._board:
            print(item)

    def check_legal(self, row, column, player):
        """Returns whether or not placing a piece to the desired position is a legal move."""# initializes if a move is legal
        if self.get_current_state() == "UNFINISHED":
            if self._board[row][column] == "":
                return True

        return False

    def make_move(self, row, column, player):
        """Places the player's piece at the desired position if it is legal, checks for a winner, and checks to see if the game is in draw."""

        if row > 15 or row < 0 or column > 15 or column < 0:
            return False # Avoid edge case in the event a desired move is outside of bounds
        if self._current_state == "UNFINISHED":
            if self.check_legal(row, column, player):
                self._board[row][column] = player

                # Check for a winner directly after placement
                if self.horizontal_win(player) == True:
                    self._current_state = str(player).upper() + "_WON"

                if self.vertical_win(player) == True:
                    self._current_state = str(player).upper() + "_WON"

                if self.diagonal_win(player) == True:
                    self._current_state = str(player).upper() + "_WON"

                # Check for draw
                if self.is_draw(player) == True:
                    self._current_state = "DRAW"
                return True
        return False

    def is_draw(self, player):
        """Checks to see if the game is draw."""
        is_draw = True # mutates if there is an empty string
        for row in self._board:
            for index in row:
                if index == "":
                    is_draw = False
        return is_draw

    def horizontal_win(self, player):
        """Returns true if there is a 5 in a row horizontally"""
        count = 0
        for row in self._board: # horizontally
            for index in row:
                if index == player:
                    count += 1
                if index != player:
                    count = 0
                if count == 5:
                    return True

    def vertical_win(self, player):
        count = 0
        """Returns true if there is a 5 in a row vertically"""
        for row in range(len(self._board)): # vertically
            for col in range(len(self._board)):
                if self._board[col][row] == player:
                    count += 1
                if self._board[col][row] != player:
                    count = 0
                if count == 5:
                    return True

    def diagonal_win(self, player):
        """Returns true if there is 5 in a row diagonally"""
        for row in range(len(self._board)): # Check \
            for col in range(len(self._board)):
                if row + 5 < 15 and col + 5 < 15:
                    if self._board[col][row] == player:
                        if self._board[col + 1][row + 1] == player and self._board[col + 2][row + 2] == player and self._board[col + 3][row + 3] == player and self._board[col + 4][row + 4] == player:
                            return True

        for row in range(len(self._board)): # Check /
            for col in range(len(self._board)):
                if row - 5 < 0 and col + 5 < 15:
                    if self._board[col][row] == player:
                        if self._board[col + 1][row - 1] == player and self._board[col + 2][row - 2] == player and self._board[col + 3][row - 3] == player and self._board[col + 4][row - 4] == player:
                            return True

#board = FiveBoard()
#board.print()

#board.make_move(4, 14, 'o')
#board.make_move(3, 14, 'o')
#board.make_move(2, 14, 'o')
#board.print()
#board.make_move(1, 14, 'o')
#board.print()
#board.make_move(0, 14, 'o')
#board.print()

#print(board.get_current_state())
