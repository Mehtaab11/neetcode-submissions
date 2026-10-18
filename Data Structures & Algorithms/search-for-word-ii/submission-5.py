class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        # Above code will generate prefix Tree for all the words
        rows, cols = len(board), len(board[0])
        visited = set()
        res = set()

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r == rows
                or c == cols
                or (r, c) in visited
                or board[r][c] not in node.children
            ):
                return

            visited.add((r, c))
            word += board[r][c]

            node = node.children[board[r][c]]
            
            if node.end == True:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)
