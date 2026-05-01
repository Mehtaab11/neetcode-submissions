class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opp = {
            "}" : "{",
            "]" : "[",
            ")" : "(",

        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif stack and opp[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
            
