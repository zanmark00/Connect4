# board.py

class Board:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.grid = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.last_move = []

    def make_move(self, move, token):
        if move < 0 or move >= self.columns or self.grid[0][move] != ' ':
            return False
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][move] == ' ':
                self.grid[row][move] = token
                self.last_move.append((row, move))
                return True
        return False

    def undo_move(self):
        if self.last_move:
            row, col = self.last_move.pop()
            self.grid[row][col] = ' '

    def check_winner(self):
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if self.grid[row][col] == self.grid[row][col + 1] == self.grid[row][col + 2] == self.grid[row][col + 3] != ' ':
                    return self.grid[row][col]
        for col in range(self.columns):
            for row in range(self.rows - 3):
                if self.grid[row][col] == self.grid[row + 1][col] == self.grid[row + 2][col] == self.grid[row + 3][col] != ' ':
                    return self.grid[row][col]
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if self.grid[row][col] == self.grid[row + 1][col + 1] == self.grid[row + 2][col + 2] == self.grid[row + 3][col + 3] != ' ':
                    return self.grid[row][col]
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if self.grid[row][col] == self.grid[row - 1][col + 1] == self.grid[row - 2][col + 2] == self.grid[row - 3][col + 3] != ' ':
                    return self.grid[row][col]
        return None

    def is_full(self):
        return all(self.grid[0][col] != ' ' for col in range(self.columns))

    def print_board(self):
        for row in self.grid:
            print('|' + '|'.join(row) + '|')
        print('+---' * self.columns + '+')

    def get_legal_moves(self):
        return [col for col in range(self.columns) if self.grid[0][col] == ' ']

    def reset(self):
        self.grid = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.last_move = []

    def is_terminal(self):
        return self.check_winner() is not None or self.is_full()

    def evaluate_heuristic(self, token):
        score = 0
        opponent_token = 'O' if token == 'X' else 'X'
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row][col] == token:
                    for d_row, d_col in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                        score += self.score_line(row, col, d_row, d_col, token)
                elif self.grid[row][col] == opponent_token:
                    for d_row, d_col in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                        score -= self.score_line(row, col, d_row, d_col, opponent_token)
        return score

    def score_line(self, row, col, d_row, d_col, token):
        score = 0
        count_token = 0
        for i in range(4):
            r, c = row + d_row * i, col + d_col * i
            if 0 <= r < self.rows and 0 <= c < self.columns:
                if self.grid[r][c] == token:
                    count_token += 1
                elif self.grid[r][c] != ' ':
                    break
        if count_token == 4:
            score += 100
        elif count_token == 3:
            score += 10
        elif count_token == 2:
            score += 1
        return score
