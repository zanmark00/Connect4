from board import Board
import random

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = self.player1
        self.winner = None

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play(self):
        while not self.board.is_full() and self.winner is None:
            print("\nCurrent board:")
            self.board.print_board()
            print(f"Player {self.current_player.get_token()}'s turn.")
            
            valid_move = False
            while not valid_move:
                move = self.current_player.make_move(self.board)
                if move is None:
                    print("Error: Player returned an invalid move. Falling back to a random move.")
                    move = random.choice(self.board.get_legal_moves())
                valid_move = self.board.make_move(move, self.current_player.get_token())
                if not valid_move:
                    print("Invalid move. Please try again.")

            winner_token = self.board.check_winner()
            if winner_token:
                self.winner = winner_token
                print("\nFinal board:")
                self.board.print_board()
                print(f"Player {winner_token} wins!")
            elif self.board.is_full():
                print("\nFinal board:")
                self.board.print_board()
                print("The game is a draw.")
            
            self.switch_player()

    def get_winner(self):
        return self.winner
