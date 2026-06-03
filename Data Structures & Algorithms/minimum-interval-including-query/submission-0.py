class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        newQ = sorted((q, i) for i, q in enumerate(queries))
        heap = []
        ans = [-1] * len(queries)
        n = len(intervals)
        i = 0
        for q, idx in newQ:
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1

            while heap and heap[0][1] < q:
                # return heap
                heapq.heappop(heap)

            if heap:
                ans[idx] = heap[0][0]

        return ans
