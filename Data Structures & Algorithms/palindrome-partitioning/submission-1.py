class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []
        part = []
        
        def isPalindrome(sub):
            return sub == sub[::-1]

        def dfs(start):
            if start == len(s):
                ans.append(part[:])
                return

            for n in range(start , len(s)):
                substring = s[start:n+1]

                if isPalindrome(substring):

                    part.append(substring)

                    dfs(n+1)

                    part.pop()


        dfs(0)
        return ans
