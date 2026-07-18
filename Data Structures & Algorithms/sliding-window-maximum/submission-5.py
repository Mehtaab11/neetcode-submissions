from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # Deque will store indices
        # Elements inside deque will always be in decreasing order
        dq = deque()
        res = []
        # Left pointer of window
        l = 0

        # Right pointer expands the window
        for r in range(len(nums)):

            # Step 1:
            # Remove smaller elements from the back
            # because they can never become maximum
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            # Step 2:
            # Add current index
            dq.append(r)

            # Step 3:
            # Remove elements outside the current window
            if dq[0] < l:
                dq.popleft()

            # Step 4:
            # Once window size becomes k
            if r - l + 1 == k:

                # Front of deque contains maximum element
                res.append(nums[dq[0]])

                # Slide window forward
                l += 1

        return res