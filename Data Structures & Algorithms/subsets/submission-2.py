class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans= []
        res = []
        def subset(nums,ans , i):
            if i == len(nums):
                res.append(ans[:])
                return 

            ans.append(nums[i])
            subset(nums,ans,i + 1)
            ans.pop()
            subset(nums,ans,i + 1)
               
        subset(nums, ans , 0)
        return res