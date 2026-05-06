class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        for num in nums:
            count = 1
            if num - 1 in seen:
                count += 1
                temp = num - 1
                while temp - 1 in seen:
                    count += 1
                    temp = temp - 1

            longest = max(longest, count)


        return longest