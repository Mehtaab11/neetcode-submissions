class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            hours = 0
            k = l + (r - l) // 2

            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res
