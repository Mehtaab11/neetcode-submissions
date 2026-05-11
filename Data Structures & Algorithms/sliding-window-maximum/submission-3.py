class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        dq = deque()
        res = []

        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)
            if dq[0] < l:
                dq.popleft()

            if r - l + 1 == k:
                res.append(nums[dq[0]])
                l += 1


        return res
