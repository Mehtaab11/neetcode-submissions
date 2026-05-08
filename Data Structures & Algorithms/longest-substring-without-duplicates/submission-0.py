class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxi = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            maxi = max(maxi, r - l + 1)

        return maxi
