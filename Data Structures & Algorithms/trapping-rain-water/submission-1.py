class Solution:
    def trap(self, ht: List[int]) -> int:
        ans = 0

        l, r = 0, len(ht) - 1

        lmx, rmx = 0, 0

        while l < r:

            lmx = max(lmx ,ht[l])
            rmx = max(rmx ,ht[r])

            if lmx < rmx :
                ans += lmx - ht[l]
                l+=1
            else:
                ans += rmx - ht[r]
                r-=1
        return ans