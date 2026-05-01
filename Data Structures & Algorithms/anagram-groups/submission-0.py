class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram= {}

        for word in strs:
            new = sorted(word)
            s_word = ''.join(new)
            if s_word not in anagram:
                anagram[s_word] = []

            anagram[s_word].append(word)

        output = anagram.values()

        return list(output)