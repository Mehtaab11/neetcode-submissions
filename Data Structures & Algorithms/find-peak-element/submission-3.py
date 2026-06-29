class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        while low < high:
            mid = low + (high - low) // 2

            elem = nums[mid]

            if elem < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid
            
        return high