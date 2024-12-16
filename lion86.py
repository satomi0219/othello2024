import math
import random

BLACK = 1
WHITE = 2

board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 0, 0],
    [0, 0, 2, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

def can_place_x_y(board, stone, x, y):
    if board[y][x] != 0:
        return False

    opponent = 3 - stone
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        found_opponent = False

        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
            nx += dx
            ny += dy
            found_opponent = True

        if found_opponent and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
            return True

    return False

def get_valid_moves(board, stone):
    valid_moves = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                valid_moves.append((x, y))
    return valid_moves

def evaluate_board(board, stone):
    """
    評価関数。
    高スコア: 良い位置 (コーナーやエッジ) を重視。
    """
    opponent = 3 - stone
    score = 0

    # 評価用の重みマトリックス
    weight = [
        [100, -20, 10, 10, -20, 100],
        [-20, -50, -2, -2, -50, -20],
        [10, -2, 1, 1, -2, 10],
        [10, -2, 1, 1, -2, 10],
        [-20, -50, -2, -2, -50, -20],
        [100, -20, 10, 10, -20, 100],
    ]

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == stone:
                score += weight[y][x]
            elif board[y][x] == opponent:
                score -= weight[y][x]

    return score

def apply_move(board, stone, x, y):
    """
    石を置き、反転を行う。
    """
    opponent = 3 - stone
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    board[y][x] = stone

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        tiles_to_flip = []

        while 0 <= nx < len(board[0]) and 0 <= ny < len(board):
            if board[ny][nx] == opponent:
                tiles_to_flip.append((nx, ny))
            elif board[ny][nx] == stone:
                for fx, fy in tiles_to_flip:
                    board[fy][fx] = stone
                break
            else:
                break

            nx += dx
            ny += dy

def alphabeta(board, stone, depth, alpha, beta, maximizing_player):
    """
    Alpha-Beta法を用いたミニマックスアルゴリズム。
    """
    valid_moves = get_valid_moves(board, stone)
    if depth == 0 or not valid_moves:
        return evaluate_board(board, stone)

    opponent = 3 - stone

    if maximizing_player:
        max_eval = -math.inf
        for x, y in valid_moves:
            temp_board = [row[:] for row in board]
            apply_move(temp_board, stone, x, y)
            eval = alphabeta(temp_board, opponent, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for x, y in valid_moves:
            temp_board = [row[:] for row in board]
            apply_move(temp_board, stone, x, y)
            eval = alphabeta(temp_board, opponent, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

class LionAI:
    def face(self):
        return "🦁"

    def place(self, board, stone):
        valid_moves = get_valid_moves(board, stone)
        if not valid_moves:
            return None

        best_move = None
        best_score = -math.inf

        for x, y in valid_moves:
            temp_board = [row[:] for row in board]
            apply_move(temp_board, stone, x, y)
            score = alphabeta(temp_board, 3 - stone, depth=6, alpha=-math.inf, beta=math.inf, maximizing_player=False)
            if score > best_score:
                best_score = score
                best_move = (x, y)

        return best_move
