class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            hours = 0
            m = l + (r - l) // 2

            for pile in piles:
                hours += math.ceil(pile / m)

            if hours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
