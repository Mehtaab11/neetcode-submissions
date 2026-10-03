class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]

        ans = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            nwMax = max(x, x * curMax , x * curMin)
            nwMin = min(x, x * curMax , x * curMin)


            curMax = nwMax
            curMin = nwMin

            ans = max(ans, curMax)

        
        return ans