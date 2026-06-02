class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals):

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][0] = min(start, res[-1][0])
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])

        return res
