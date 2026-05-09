class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        l = r = 0

        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            # Putting index of every new element in deck
            # removal will happen on the next loop , but why?
            # Shouldn't we be checking now
            # We do append the new index after removing the weaker element
            # because up above we compared to the value of this index
            # whether greater or onot
            dq.append(r)

            # Out of bound Removal
            if dq[0] < l:
                dq.popleft()

            # Why here we do r + 1 >= k
            # Which is going to be true in most of the cases
            if (r - l) + 1 == k:
                res.append(nums[dq[0]])
                l += 1

            r += 1

        return res
