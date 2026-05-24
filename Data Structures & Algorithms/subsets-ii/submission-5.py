class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = []
        nums.sort()

        def subset(nums, ans, i):
            if i == len(nums):
                res.append(ans[:])
                return

            # suppose it is [2,2]
            # below code is responsible for taking 2
            ans.append(nums[i])
            subset(nums, ans, i + 1)

            # remove the element we took above
            # below code is responsible for not taking 2
            ans.pop()
            # keep removing till we keep finding duplicates
            # this code is responsible for keep removing till we find duplicates
            while i + 1 < len(nums) and nums[i] == nums[i +1] :
                i+=1
            subset(nums, ans, i + 1)

        subset(nums, ans, 0)
        return res
