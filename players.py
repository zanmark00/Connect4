# players.py

from minimax import MinimaxStrategy
from qlearning import QLearningStrategy
import random

class Player:
    def __init__(self, token):
        self.token = token

    def make_move(self, board):
        pass

    def get_token(self):
        return self.token

class PlayerManager:
    def __init__(self):
        self.players = {}

    def create_player(self, player_type, token, **kwargs):
        if player_type == 'qlearning':
            learning_rate = kwargs.get('learning_rate', 0.1)
            discount_factor = kwargs.get('discount_factor', 0.9)
            epsilon = kwargs.get('epsilon', 0.1)
            strategy = QLearningStrategy(learning_rate, discount_factor, epsilon, token)
            player = QLearningPlayer(token, strategy)
        elif player_type == 'minimax':
            depth_limit = kwargs.get('depth_limit', 3)
            player = MinimaxPlayer(token, depth_limit)
        elif player_type == 'default':
            player = DefaultPlayer(token)
        else:
            raise ValueError(f"Unsupported player type: {player_type}")
        self.players[token] = player
        return player

class DefaultPlayer(Player):
    def make_move(self, board):
        legal_moves = board.get_legal_moves()
        return random.choice(legal_moves) if legal_moves else None

class MinimaxPlayer(Player):
    def __init__(self, token, depth_limit=3):
        super().__init__(token)
        self.strategy = MinimaxStrategy(token)
        self.depth_limit = depth_limit

def make_move(self, board):
    _, best_move = self.strategy.minimax(board, self.depth_limit, True)
    return best_move

class QLearningPlayer(Player):
    def __init__(self, token, strategy):
        super().__init__(token)
        self.strategy = strategy

    def make_move(self, board):
        state_hash = self.strategy._hash_state(board)
        legal_moves = board.get_legal_moves()
        return self.strategy.choose_action(state_hash, legal_moves)
