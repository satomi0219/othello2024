class AI(object):

    def face(self):
        return "😻"

    def place(self, board, stone):
        return x, y

class HeartCatAI(object):
    def __init__(self):
        # ボードの評価マップ (スコアの高い場所を優先)
        self.score_map = [
            [100, -20, 10, 10, -20, 100],
            [-20, -50, -2, -2, -50, -20],
            [10, -2,  0,  0,  -2,  10],
            [10, -2,  0,  0,  -2,  10],
            [-20, -50, -2, -2, -50, -20],
            [100, -20, 10, 10, -20, 100],
        ]

    def face(self):
        return "😻"

    def evaluate_move(self, board, stone, x, y):
        """
        その場所に石を置いたときのスコアを評価する。
        """
        return self.score_map[y][x]

    def get_possible_moves(self, board, stone):
        """
        現在の石で置けるすべての座標を取得する。
        """
        moves = []
        for y in range(len(board)):
            for x in range(len(board[0])):
                if can_place_x_y(board, stone, x, y):
                    moves.append((x, y))
        return moves

    def place(self, board, stone):
        """
        最善の場所を計算して石を置く。
        """
        possible_moves = self.get_possible_moves(board, stone)
        if not possible_moves:
            raise ValueError("No possible moves")

        # 各手を評価してスコアの高いものを選ぶ
        best_move = None
        best_score = float('-inf')
        for x, y in possible_moves:
            score = self.evaluate_move(board, stone, x, y)
            if score > best_score:
                best_score = score
                best_move = (x, y)

        return best_move
