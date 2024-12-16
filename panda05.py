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
def can_place(board, stone):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                return True
    return False

def place_stone(board, stone, x, y):
    if not can_place_x_y(board, stone, x, y):
        raise ValueError("Invalid move")

    opponent = 3 - stone
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    board[y][x] = stone  

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        stones_to_flip = []

        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
            stones_to_flip.append((nx, ny))
            nx += dx
            ny += dy

        if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
            for fx, fy in stones_to_flip:
                board[fy][fx] = stone  

def evaluate_move(board, stone, x, y):
    corner_positions = [(0, 0), (0, 5), (5, 0), (5, 5)]
    edge_positions = [(0, i) for i in range(6)] + [(5, i) for i in range(6)] + [(i, 0) for i in range(6)] + [(i, 5) for i in range(6)]

    if (x, y) in corner_positions:
        return 100  
    elif (x, y) in edge_positions:
        return 10  
    else:
        return 1  

class SmartAI(object):

    def face(self):
        return "🦉"

    def place(self, board, stone):
        legal_moves = [(x, y) for y in range(len(board)) for x in range(len(board[0])) if can_place_x_y(board, stone, x, y)]

        if not legal_moves:
            raise ValueError("No legal moves available")

        best_move = max(legal_moves, key=lambda move: evaluate_move(board, stone, *move))
        return best_move

ai = SmartAI()
stone = BLACK
x, y = ai.place(board, stone)
place_stone(board, stone, x, y)

for row in board:
    print(row)
