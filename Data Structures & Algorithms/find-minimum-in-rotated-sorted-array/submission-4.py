class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums) 

        if nums[0] < nums[n - 1]:
            return nums[0]

        low = 0 
        high = n - 1

        while low < high:
            mid = low + (high - low) // 2
            elem = nums[mid]

            if elem > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        return nums[low]








