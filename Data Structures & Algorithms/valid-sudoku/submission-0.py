class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        block = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in block[(r//3,c//3)]:
                    return False
                if board[r][c] == '.':
                    continue
                else:
                    cell = board[r][c]
                    rows[r].add(cell)
                    cols[c].add(cell)
                    block[(r//3,c//3)].add(cell)
        print(rows)
        print(cols)
        return True
        