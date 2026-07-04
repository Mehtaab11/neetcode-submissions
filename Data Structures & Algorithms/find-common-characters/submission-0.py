class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for word in words[1:]:
            count = count & Counter(word)

        ans = []

        for ch,freq in count.items():
            ans.extend([ch] * freq)
        
        return ans