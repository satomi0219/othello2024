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
            [10, 5, 5, 5, 5, 10],
    [5, 1, 2, 2, 1, 5],
    [5, 2, 0, 0, 2, 5],
    [5, 2, 0, 0, 2, 5],
    [5, 1, 2, 2, 1, 5],
    [10, 5, 5, 5, 5, 10]
    ]

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == stone:
                score += weight[y][x]
            elif board[y][x] == opponent:
                score -= weight[y][x]

    return score

class PandaAI:
    def face(self):
        return "🐼"

    def place(self, board, stone):
        valid_moves = get_valid_moves(board, stone)
        if not valid_moves:
            return None

        # 各手を試して評価する
        best_move = None
        best_score = -math.inf

        for x, y in valid_moves:
            # 仮に置いてみる
            temp_board = [row[:] for row in board]
            temp_board[y][x] = stone

            # 評価
            score = evaluate_board(temp_board, stone)

            if score > best_score:
                best_score = score
                best_move = (x, y)

        return best_move
