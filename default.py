import random

class DefaultPlayer(Player):
    def __init__(self, token):
        super().__init__(token)

    def find_winning_move(self, board):
        for col in range(board.columns):
            if board.can_place_token(col) and board.is_winning_move(col, self.token):
                return col
        return None

    def find_blocking_move(self, board):
        opponent_token = 'O' if self.token == 'X' else 'X'
        for col in range(board.columns):
            if board.can_place_token(col) and board.is_winning_move(col, opponent_token):
                return col
        return None

    def make_move(self, board):
        # Attempt to find a winning move
        winning_move = self.find_winning_move(board)
        if winning_move is not None:
            return winning_move

        # If no winning move, attempt to block opponent's winning move
        blocking_move = self.find_blocking_move(board)
        if blocking_move is not None:
            return blocking_move

        # Fallback: choose a random valid move
        valid_moves = board.get_legal_moves()
        return random.choice(valid_moves) if valid_moves else None
