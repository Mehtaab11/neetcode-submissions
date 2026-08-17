class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        def dfs(idx, n):
            if idx >= n:
                return 0

            if idx in memo:
                return memo[idx]

            skip = dfs(idx + 1, n)
            steal = nums[idx] + dfs(idx + 2, n)

            memo[idx] = max(steal, skip)
            return memo[idx]

        memo = {}
        case1 = dfs(0, len(nums) - 1)

        memo = {}
        case2 = dfs(1, len(nums))

        return max(case1,case2)
