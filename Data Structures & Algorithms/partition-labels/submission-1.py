class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = {}

        for i in range(len(s)):
            map[s[i]] = i

        i = 0
        res = []
        while i < len(s):
            end = map[s[i]]
            j = i
            while j < len(s) and j <= end:
                end = max(end, map[s[j]])
                j += 1

            res.append(j - i)
            i = j 

        return res
