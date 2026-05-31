class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            cur = node

            for i in range(idx, len(word)):
                ch = word[i]

                if ch == ".":

                    for child in cur.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            
            return cur.end

        return dfs(self.root, 0)
