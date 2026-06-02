class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])
        ans = len(intervals)
        pre = float("-inf")

        for start, end in intervals:
            if start >= pre:
                pre = end
                ans -= 1

        return ans
