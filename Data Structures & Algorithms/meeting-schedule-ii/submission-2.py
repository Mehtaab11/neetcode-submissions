"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        end = max(e.end for e in intervals)

        dArr = [0] * (end + 1)

        for interval in intervals:
            l , r  = interval.start , interval.end
            dArr[l] += 1
            dArr[r] -= 1

        res = 0
        ans = 0

        for val in dArr:
            res += val
            ans = max(ans, res)

        return ans
