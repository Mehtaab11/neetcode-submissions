from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(current):
            if current >= len(cost):
                return 0

            
            one_step = dfs(current+ 1)
            two_step = dfs(current+ 2)

            return cost[current] + min(one_step , two_step)
        
        step1 = dfs(0)
        step2 = dfs(1)

        return min(step1,step2)