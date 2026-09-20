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

        d = [0] * (end + 1)

        for interval in intervals:
            l, r = interval.start, interval.end
            d[l] += 1
            d[r] -= 1
        
        ans = res = 0

        for val in d:
            res += val

            ans = max(ans,res)

        return ans

