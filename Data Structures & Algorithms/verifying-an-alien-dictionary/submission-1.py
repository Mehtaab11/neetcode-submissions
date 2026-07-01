class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {ch: i for i,ch in enumerate(order)}

        for i in range(len(words) -1):
            w1 = words[i]
            w2 = words[i + 1]

            minLen = min(len(w1) , len(w2))

            j = 0

            while j < minLen:
                if w1[j] != w2[j]:
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break
                j +=1
            else:
                if len(w1) > len(w2):
                    return False
        
        return True