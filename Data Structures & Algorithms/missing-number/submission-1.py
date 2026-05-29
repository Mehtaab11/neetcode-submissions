class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        check = n * (n + 1) // 2

        return check - total
