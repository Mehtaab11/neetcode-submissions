class Solution:
    def rob(self, nums: List[int]) -> int:

        maxi = float("-inf")

        memo  = {}
        def dfs(idx):
            nonlocal maxi
            if idx >= len(nums):
                return 0

            if idx in memo :
                return memo[idx]
            skip = dfs(idx + 1)
            steal = dfs(idx + 2)

            maxi = max(steal + nums[idx], skip)
            memo[idx] = maxi
            return memo[idx]

        dfs(0)

        return maxi
