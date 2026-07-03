class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def fib(i):
            if i <= 1:
                return 1

            if i in memo:
                return memo[i]

            memo[i] = fib(i - 1) + fib(i - 2)

            return memo[i]

        return fib(n)
