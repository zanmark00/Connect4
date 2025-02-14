# qlearning.py

import random
import hashlib
import math
from game import Game

class QLearningStrategy:
    def __init__(self, learning_rate=0.1, discount_factor=0.9, epsilon=0.1, token='X'):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.token = token
        self.q_values = {} 
        self.learning_rate_decay = 0.999
        self.epsilon_decay = 0.9995
        self.min_epsilon = 0.01
        self.min_learning_rate = 0.005

    def _hash_state(self, board):
        state_representation = ''.join(''.join(row) for row in board.grid)
        return hashlib.sha256(state_representation.encode('utf-8')).hexdigest()

    def choose_action(self, state_hash, legal_moves):
        if random.random() < self.epsilon:
            return random.choice(legal_moves)
        else:
            return self.best_action(state_hash, legal_moves)

    def best_action(self, state_hash, legal_moves):
        best_action = None
        max_q_value = -float('inf')
        for action in legal_moves:
            q_value = self.q_values.get((state_hash, action), 0)
            if q_value > max_q_value:
                best_action = action
                max_q_value = q_value
        return best_action

    def update_q_value(self, state_hash, action, reward, next_state_hash, legal_moves_next_state):
        old_q = self.q_values.get((state_hash, action), 0)
        future_q_values = [self.q_values.get((next_state_hash, a), 0) for a in legal_moves_next_state]
        max_future_q = max(future_q_values, default=0)
        new_q = old_q + self.learning_rate * (reward + self.discount_factor * max_future_q - old_q)
        self.q_values[(state_hash, action)] = new_q

    def update_learning_parameters(self, episode, total_episodes):
        self.epsilon = max(self.min_epsilon, self.epsilon * self.epsilon_decay)
        self.learning_rate = max(self.min_learning_rate, self.learning_rate * self.learning_rate_decay)

    def train(self, game, train_episodes):
        for episode in range(1, train_episodes + 1):
            self.update_learning_parameters(episode, train_episodes)
            game.board.reset()
            while not game.board.is_terminal():
                state_hash = self._hash_state(game.board)
                legal_moves = game.board.get_legal_moves()
                action = self.choose_action(state_hash, legal_moves)
                game.board.make_move(action, self.token)
                winner = game.board.check_winner()
                reward = self.calculate_reward(game.board, winner)
                next_state_hash = self._hash_state(game.board)
                self.update_q_value(state_hash, action, reward, next_state_hash, game.board.get_legal_moves())

    def calculate_reward(self, board, winner):
        if winner == self.token:
            return 1 
        elif board.is_full():
            return 0  
        return -1 
