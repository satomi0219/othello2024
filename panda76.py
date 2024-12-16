class EagerAI(object):

    def face(self):
        return "🐼"

    def place(self, board, stone):
        """
        石を最も多く取れる位置に置く
        """
        best_score = -1
        best_move = None

        for y in range(len(board)):
            for x in range(len(board[0])):
                if can_place_x_y(board, stone, x, y):
                    score = self.evaluate_move(board, stone, x, y)
                    if score > best_score:
                        best_score = score
                        best_move = (x, y)

        return best_move

    def evaluate_move(self, board, stone, x, y):
        """
        指定の位置に石を置いた場合に取れる石の数を計算する
        """
        opponent = 3 - stone  # 相手の石 (1なら2、2なら1)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            local_count = 0

            # 相手の石を数える
            while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
                nx += dx
                ny += dy
                local_count += 1

            # 最後に自分の石で囲める場合のみカウント
            if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
                count += local_count

        return count
