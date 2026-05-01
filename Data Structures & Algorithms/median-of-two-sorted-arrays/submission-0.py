class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)

        if size1 > size2:
            return self.findMedianSortedArrays(nums2, nums1)

        l  = 0 
        r = size1

        n  = (size1 + size2 + 1) // 2
        while l <= r:
            mid1 = (l + r )// 2
            mid2 = n - mid1
            l1 = float('-inf') if mid1 == 0 else nums1[mid1-1]
            r1 = float('inf') if mid1 == size1 else nums1[mid1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r2 = float('inf') if mid2 == size2 else nums2[mid2]

            if l1 <= r2 and l2 <= r1:
                if (size1 + size2) % 2 == 1:
                    return max(l1,l2)
                return (max(l1,l2) + min(r1,r2)) / 2
            elif l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1


        return 0


