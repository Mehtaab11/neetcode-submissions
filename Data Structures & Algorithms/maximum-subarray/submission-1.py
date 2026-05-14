class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxi = res
        for num in nums[1:]:
            if maxi < 0:
                maxi = 0

            maxi += num

            res = max(maxi, res)

        return res
