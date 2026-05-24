class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = []
        nums.sort()

        def subset(nums, ans, i):
            if i == len(nums):
                res.append(ans[:])
                return

            ans.append(nums[i])
            subset(nums, ans, i + 1)

            # remove the element we took above
            ans.pop()
            # keep removing till we keep finding duplicates
            while i + 1 < len(nums) and nums[i] == nums[i +1] :
                i+=1
            subset(nums, ans, i + 1)

        subset(nums, ans, 0)
        return res
