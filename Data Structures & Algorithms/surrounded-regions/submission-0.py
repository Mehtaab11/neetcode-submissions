class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or c == cols or r == rows or (r, c) in visited or board[r][c] != "O":
                return

            visited.add((r, c))
            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"
        

