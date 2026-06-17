class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append([v, t])

        distance = [float("inf")] * (n)

        distance[k - 1] = 0

        min_heap = [(0, k)]

        while min_heap:
            curr_time, node = heapq.heappop(min_heap)

            if curr_time > distance[node - 1]:
                continue

            for nei, time in graph[node]:
                new_time = curr_time + time

                if new_time < distance[nei - 1]:
                    distance[nei - 1] = new_time
                    heapq.heappush(min_heap, (new_time, nei))

        max_distance = max(distance)
        return -1 if max_distance == float("inf") else max_distance
