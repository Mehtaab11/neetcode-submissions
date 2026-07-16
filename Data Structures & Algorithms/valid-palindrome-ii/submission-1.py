class Solution:
    def validPalindrome(self, s: str) -> bool:

        if self.isPali(s):
            return True

        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1

            if s[l] != s[r]:
                return (self.isPali(s[l+1 : r+1]) or self.isPali(s[l:r]))
        
        return False

    def isPali(self, s):
        return s == s[::-1]
