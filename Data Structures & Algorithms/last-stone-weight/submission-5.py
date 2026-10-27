class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones: #n
            heapq.heappush(max_heap, -stone) # log n
        # n log n

        while len(max_heap) > 1:
            x = -(heapq.heappop(max_heap))
            y = -(heapq.heappop(max_heap))

            if x != y:
                heapq.heappush(max_heap, -(x - y))

                #3 log n operations

        # n log n 
        

        return -max_heap[0] if max_heap else 0
