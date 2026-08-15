class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}

        def dfs(i):
            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]

            one_step = dfs(i + 1)
            two_step = dfs(i + 2)

            memo[i] = cost[i] + min(one_step, two_step)

            return memo[i]

        one = dfs(0)
        two = dfs(1)

        return min(one, two)
