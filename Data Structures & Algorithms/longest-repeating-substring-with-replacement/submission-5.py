class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0

        mf = 0
        best = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            mf = max(freq.values())

            if (right - left + 1) - mf > k:
                freq[s[left]] -= 1
                left += 1


            best = max(best , right-left + 1)
        

        return best