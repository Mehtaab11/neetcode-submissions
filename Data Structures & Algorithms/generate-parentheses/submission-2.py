class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s , opencount , closecount):
            if len(s) == n * 2:
                res.append(s[:])                
                return

            if opencount < n:
                backtrack(s + "(" , opencount + 1 , closecount)

            if closecount < opencount:
                backtrack(s + ")" , opencount , closecount + 1)

        backtrack("" , 0 , 0)
        return res