class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minHeap = [(0, 0)]

        visited = [False] * n
        total = 0

        while minHeap:
            cost, node = heapq.heappop(minHeap)

            if visited[node]:
                continue

            visited[node] = True

            total += cost
            x1, y1 = points[node]
            for nei in range(n):
                if not visited[nei]:
                    x2, y2 = points[nei]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (dist, nei))
        

        return total