class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans= []
        res = []
        nums.sort()
        def subset(nums,ans , i):
            if i == len(nums):
                res.append(ans[:])
                return 

            ans.append(nums[i])
            subset(nums,ans,i + 1)
            
            ans.pop()
            idx = i + 1

            while idx < len(nums) and nums[idx] == nums[idx - 1]:
                idx +=1
            subset(nums,ans,idx)

               
        subset(nums, ans , 0)
        return res  