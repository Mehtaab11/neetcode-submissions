class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        s = -1
        h = -1
        while low <= high:
            mid = low + (high - low) // 2
            elem = nums[mid]

            if elem == target:
                h = mid
                low = mid + 1
            elif elem > target:
                high = mid - 1
            else:
                low = mid + 1

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            elem = nums[mid]

            if elem == target:
                s = mid
                high = mid - 1
            elif elem > target:
                high = mid - 1
            else:
                low = mid + 1

        return [s, h]
