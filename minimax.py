import math

class MinimaxStrategy:
    def __init__(self, token, use_alpha_beta=True):
        self.token = token
        self.opponent_token = 'O' if token == 'X' else 'X'
        self.transposition_table = {}
        self.use_alpha_beta = use_alpha_beta

    def select_move(self, board, max_depth=10):
        best_move = None
        for depth in range(5, max_depth + 1):
            if self.use_alpha_beta:
                move = self.minimax_alpha_beta(board, self.token, float('-inf'), float('inf'), depth)[0]
            else:
                move = self.minimax(board, self.token, float('-inf'), float('inf'), depth)[0]
            if move is not None:
                best_move = move
        return best_move

    def minimax(self, board, player, alpha, beta, depth):
        if depth == 0:
            return None, self.evaluate(board, player)
        board_hash = board.get_hash()
        if board_hash in self.transposition_table:
            return self.transposition_table[board_hash]
        winner = board.check_winner()
        if winner:
            score = self.evaluate(board, player)
            self.transposition_table[board_hash] = (None, score)
            return None, score
        best_move = None
        if player == self.token:
            best_score = float('-inf')
            for move in board.get_legal_moves():
                board.make_move(move, player)
                _, score = self.minimax(board, self.opponent_token, alpha, beta, depth-1)
                board.undo_move()
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        else:
            best_score = float('inf')
            for move in board.get_legal_moves():
                board.make_move(move, player)
                _, score = self.minimax(board, self.token, alpha, beta, depth-1)
                board.undo_move()
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        self.transposition_table[board_hash] = (best_move, best_score)
        return best_move, best_score

    def minimax_alpha_beta(self, board, player, alpha, beta, depth):
        if depth == 0:
            return None, self.evaluate(board, player)
        board_hash = board.get_hash()
        if board_hash in self.transposition_table:
            return self.transposition_table[board_hash]
        winner = board.check_winner()
        if winner:
            score = self.evaluate(board, player)
            self.transposition_table[board_hash] = (None, score)
            return None, score
        best_move = None
        if player == self.token:
            best_score = float('-inf')
            for move in board.get_legal_moves():
                board.make_move(move, player)
                _, score = self.minimax_alpha_beta(board, self.opponent_token, alpha, beta, depth-1)
                board.undo_move()
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        else:
            best_score = float('inf')
            for move in board.get_legal_moves():
                board.make_move(move, player)
                _, score = self.minimax_alpha_beta(board, self.token, alpha, beta, depth-1)
                board.undo_move()
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        self.transposition_table[board_hash] = (best_move, best_score)
        return best_move, best_score

    def evaluate(self, board, player):
        winner = board.check_winner()
        if winner == self.token:
            return 10000
        elif winner == self.opponent_token:
            return -10000
        else:
            return self.evaluate_position(board, player) - self.evaluate_position(board, self.opponent_token)

    def evaluate_position(self, board, player):
        score = 0
        row_count = len(board.board)
        col_count = len(board.board[0])
        for row in range(row_count):
            for col in range(col_count):
                if row <= row_count - 4:
                    score += self.evaluate_line([board.board[row + i][col] for i in range(4)], player)
                if col <= col_count - 4:
                    score += self.evaluate_line([board.board[row][col + i] for i in range(4)], player)
                if row <= row_count - 4 and col <= col_count - 4:
                    score += self.evaluate_line([board.board[row + i][col + i] for i in range(4)], player)
                if row <= row_count - 4 and col >= 3:
                    score += self.evaluate_line([board.board[row + i][col - i] for i in range(4)], player)
        return score

    def evaluate_line(self, line, player):
        score = 0
        opponent = self.opponent_token if player == self.token else self.token
        if line.count(player) == 4:
            score += 1000000
        elif line.count(player) == 3 and line.count(' ') == 1:
            score += 1000
        elif line.count(player) == 2 and line.count(' ') == 2:
            score += 100
        if line.count(opponent) == 3 and line.count(' ') == 1:
            score -= 500
        return score
