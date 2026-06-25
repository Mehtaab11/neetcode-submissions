class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):

            last = n & 1

            pos = last << (31 - i)

            ans = ans | pos
            n = n >> 1

        return ans