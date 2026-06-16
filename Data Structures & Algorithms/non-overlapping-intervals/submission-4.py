class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])
        # we consider all elements to remove
        # We will decrement it as we move and encounter no Overlapping
        ans = len(intervals)
        pre = float("-inf")

        for start, end in intervals:
            # given below condition checks if
            # there exists and overlap or not
            # given code here tell that there is no overlap
            # thus we reverse engineer it a bit and decrease the count
            # if current interval's start is more than pre's end which
            # means there is no overlapping and we can move forward
            # Also excluding it from our original count of intervals to be remove
            if start >= pre:
                pre = end
                ans -= 1

        return ans
