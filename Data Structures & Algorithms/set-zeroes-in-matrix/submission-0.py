class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row = len(matrix)
        col = len(matrix[0])

        rows = [False] * row
        columns = [False] * col


        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    rows[r] = True
                    columns[c] = True

        
        for r in range(row):
            for c in range(col):
                if rows[r] or columns[c]:
                    matrix[r][c] = 0



