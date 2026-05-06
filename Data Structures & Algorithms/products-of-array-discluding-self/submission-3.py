class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans= [1] * n


        for i in range(1,n):
            ans[i] = nums[i-1] * ans[i-1]

        suffix = 1

        for i in range(n-2 ,-1 , -1):
            suffix *= nums[i+1]
            ans[i] *=  suffix

        return ans