class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == '':
            return []
        
        ans = []
        mp = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def solve(idx , s , temp):
            if idx >=len(s):
                ans.append(temp)
                return

            letters = mp[digits[idx]]

            for char in letters:
                temp = temp + char
                solve(idx +1 , s ,temp)
                temp  = temp[:-1]


        solve(0 , digits, '' )

        return ans