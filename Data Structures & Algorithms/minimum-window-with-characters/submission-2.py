class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)

        mp = defaultdict(int)

        required = len(target)

        
        formed = 0

        best = float("inf")

        left_best = 0
        right_best = 0

        left = 0

        for right in range(len(s)):
            char = s[right]
            mp[char] += 1

            if char in target and mp[char] == target[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < best:
                    best = right - left + 1
                    left_best = left
                    right_best = right

                left_char = s[left]
                mp[left_char] -= 1

                if left_char in target and mp[left_char] < target[left_char]:
                    formed -= 1

                left += 1

        if best == float("inf"):
            return ""

      
        return s[left_best : right_best + 1]
