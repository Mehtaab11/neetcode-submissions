class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])
        ans = len(intervals)
        pre = float("-inf")

        for start, end in intervals:
            # given below condition checks if
            # there exists and overlap or not
            # given code here tell that there is no overlap
            # thus we reverse engineer it a bit and decrease the count
            if start >= pre:
                pre = end
                ans -= 1

        return ans
