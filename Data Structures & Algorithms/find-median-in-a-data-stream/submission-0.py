import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max heap (invert values)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # step 1: push into max heap (small side)
        heapq.heappush(self.small, -num)

        # step 2: balance ordering
        # ensure every element in small <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # step 3: balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # if even elements
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0

        # if small has more
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        # if large has more
        return float(self.large[0])