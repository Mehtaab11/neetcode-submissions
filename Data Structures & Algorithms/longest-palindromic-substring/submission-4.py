class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        memo = [[None] * n for _ in range(n)]

        def isPal(i, j):
            if i >= j:
                return True

            if memo[i][j] is not None:
                return memo[i][j]

            if s[i] == s[j]:
                memo[i][j] = isPal(i + 1, j - 1)
            else:
                memo[i][j] = False

            return memo[i][j]

        max_length = 0
        best_start = 0

        for i in range(n):
            for j in range(i, n):
                if isPal(i, j):
                    length = j - i + 1
                    if length > max_length:
                        max_length = length
                        best_start = i

        return s[best_start : max_length + best_start]
