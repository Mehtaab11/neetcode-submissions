class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n > 1:
            # # remove the last set bit which will be one
            # n = n & n - 1
            # # the line above beautifullt removes the last set bit in an integer
            # # everytime it is removed increment the count by 1
            # cnt += 1

            cnt += n & 1

            n = n >> 1

        if n == 1:
            cnt += 1

        return cnt
