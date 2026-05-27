class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # Stores which columns already have queens
        cols = set()

        # Stores positive diagonals (row + col)
        # Example:
        # (0,1) -> 1
        # (1,0) -> 1
        # Same value means same positive diagonal
        posDiag = set()

        # Stores negative diagonals (row - col)
        # Example:
        # (1,0) -> 1
        # (2,1) -> 1
        # Same value means same negative diagonal
        negDiag = set()

        # Final list of valid boards
        res = []

        # Create empty chess board
        board = [["."] * n for i in range(n)]

        # r = current row we are trying to place queen in
        def backtracking(r):

            # Base case:
            # If we placed queens in all rows,
            # we found one valid solution
            if r == n:

                # Convert board rows from list -> string
                # Example: ['Q', '.', '.'] -> "Q.."
                copy = ["".join(row) for row in board]

                # Store the solution
                res.append(copy)
                return

            # Try placing queen in every column
            # of current row
            for c in range(n):

                # If column or diagonal already occupied,
                # skip this position
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Place queen
                # Mark column and diagonals as occupied
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                # Put queen on board
                board[r][c] = "Q"

                # Move to next row
                backtracking(r + 1)

                # BACKTRACKING STEP
                # Remove queen and free column/diagonals
                # so we can try next possibility

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

                # Reset board cell
                board[r][c] = "."

        # Start solving from row 0
        backtracking(0)

        return res