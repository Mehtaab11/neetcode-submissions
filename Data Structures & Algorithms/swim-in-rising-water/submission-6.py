class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)]
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if r == n - 1 and c == n - 1:
                return t

            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc

                if neiR < 0 or neiC < 0 or neiR == n or neiC == n or (neiR, neiC) in visit:
                    continue

                elem = max(grid[neiR][neiC], t)

                heapq.heappush(minHeap, (elem, neiR, neiC))
