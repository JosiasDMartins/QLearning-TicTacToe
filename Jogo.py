import numpy as np
import random

class JogoDaVelha:   
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # 1 for X, -1 for O
        self.winner = None
        self.game_over = False

    def is_valid_move(self, row, col):
        return self.board[row][col] == 0

    def make_move(self, row, col):
        if not self.game_over and self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.check_winner()
            self.current_player *= -1  # Switch player

    def check_winner(self):
        for i in range(3):
            if all(self.board[i, :] == self.current_player) or \
               all(self.board[:, i] == self.current_player):
                self.winner = self.current_player
                self.game_over = True
                return

        if all(np.diag(self.board) == self.current_player) or \
           all(np.diag(np.fliplr(self.board)) == self.current_player):
            self.winner = self.current_player
            self.game_over = True
            return

        if np.all(self.board != 0):
            self.game_over = True

    def print_board(self):
        for row in self.board:
            print(" | ".join(["X" if cell == 1 else "O" if cell == -1 else " " for cell in row]))
            print("-" * 9)


def play_game(agent):
    game = JogoDaVelha()
    while not game.game_over:
        game.print_board()
        if game.current_player == 1:
            while True:
                try:
                    row, col = map(int, input("Enter your move (row and column, space-separated): ").split())
                    if (0 <= row < 3) and (0 <= col < 3) and game.is_valid_move(row, col):
                        game.make_move(row, col)
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Enter your move as two space-separated integers.")
        else:
            state = game.board.copy()
            action = agent.choose_action(state)
            game.make_move(action // 3, action % 3)

    game.print_board()
    if game.winner == 1:
        print("You win!")
    elif game.winner == -1:
        print("Agent wins!")
    else:
        print("It's a tie!")
