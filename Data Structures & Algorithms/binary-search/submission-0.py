class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums)-1

        while low <= high:

            mid = low + (high - low) // 2

            elem = nums[mid]

            if elem < target :
                low = mid + 1
            elif elem > target:
                high = mid -1
            else :
                return mid

        return -1
        