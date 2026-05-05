class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram= {}

        for word in strs:
            new = sorted(word)  # this here is going to return a list
            s_word = ''.join(new) # thats why we join it here 
            if s_word not in anagram: # if this is the first time seeing a combination create a key for that
                anagram[s_word] = []

            anagram[s_word].append(word) # this one always run because no matter what we are going to append it in a list

        output = anagram.values() # get the values only 

        return list(output) # make a list and return