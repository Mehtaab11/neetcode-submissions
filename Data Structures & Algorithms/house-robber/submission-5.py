from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:

        maxi = float("-inf")

        @cache
        def dfs(idx):
            nonlocal maxi
            if idx >= len(nums):
                return 0

            steal = dfs(idx + 2)
            skip = dfs(idx + 1)
            maxi = max(steal + nums[idx], skip)

            return maxi

        dfs(0)

        return maxi
