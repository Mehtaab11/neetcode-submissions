class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def subset( target, ans,  i):
            if target == 0:
                res.append(ans[:])
                return
                
            if i == len(nums) or target < 0:
                return 


            ans.append(nums[i])
            subset(target - nums[i] , ans, i + 1)

            ans.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i+=1
            subset( target ,ans, i + 1)
               
        subset( target, [] , 0)
        return res