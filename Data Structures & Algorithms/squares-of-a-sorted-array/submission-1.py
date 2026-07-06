class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        l = 0
        r = len(nums)-1

        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2:
                nums[l] = nums[l] ** 2
                l += 1
            else:
                temp = nums[r] ** 2
                nums[r] = nums[l]
                nums[l] = temp
                l+=1
        
        return sorted(nums)