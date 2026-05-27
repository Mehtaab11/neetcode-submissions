class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for i in range(n)]

        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r +c) in posDiag or (r - c) in negDiag:
                    continue

                # My mistake was that when we found already used column
                # I was returning but i needed to skip the iteration

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                board[r][c] = "Q"
                backtracking(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtracking(0)

        return res
