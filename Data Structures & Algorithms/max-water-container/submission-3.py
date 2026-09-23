class Solution:
    def maxArea(self, ht: List[int]) -> int:
        n = len(ht)

        l, r = 0, n - 1
        maxi = 0
        while l < r:
            height = min(ht[l], ht[r])
            area = height * (r - l)
            maxi = max(maxi, area)

            if ht[l] < ht[r]:
                l += 1
            else:
                r -= 1

        return maxi

# class Solution:
#     def maxArea(self, ht: List[int]) -> int:
#         n = len(ht)

#         l, r = 0, n - 1
#         maxi = 0

#         while l < r:
#             if ht[l] < ht[r]:
#                 area = ht[l] * (r - l)
#                 maxi = max(maxi, area)
#                 l += 1
#             else:
#                 area = ht[r] * (r - l)
#                 maxi = max(maxi, area)
#                 r -= 1

#         return maxi