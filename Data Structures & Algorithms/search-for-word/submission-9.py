class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def backtrack(r, c, i):
            # here we will return once the i becomes equal to length of the word
            # but notice the i will only be incremented after we have already taken the char
            # so basically even after we have completed the search we are
            # going to give one extra call to check this
            if i == len(word):
                return True

            # here we are checking index because 0 based indexing
            # number at 2 is letter number 3 in word
            # basically we find the letter 3 and then we call again to check if we have#
            # reached the length of the word or not
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c]
                # or (r, c) in path
            ):
                return

            if (r, c) in path:
                return

            path.add((r, c))

            res = (
                backtrack(r + 1, c, i + 1)
                or backtrack(r - 1, c, i + 1)
                or backtrack(r, c + 1, i + 1)
                or backtrack(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0) == True:
                    return True
        # pass on the index of r , c and the letter position that we are currently looking for

        return False
