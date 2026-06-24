class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        dist = [float("inf")] * n

        dist[src] = 0

        for i in range(k + 1):
            temp = dist[:]

            for s, d, p in flights:
                if dist[s] == float("inf"):
                    continue

                temp[d] = min(temp[d], dist[s] + p)

            dist = temp

        return -1 if dist[dst] == float("inf") else dist[dst]
