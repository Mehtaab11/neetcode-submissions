class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        n = len(intervals)
        i = 0
        res = []
        # Responsible for going past all the intervals that
        #  are going to end before our new interval start
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        # Once we have reached the right place we will add the newInterval to its place
        res.append(newInterval)

        # Once we have appended we can safely insert all of the
        # remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1
        return res
