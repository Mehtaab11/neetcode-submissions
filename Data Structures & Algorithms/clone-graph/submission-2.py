"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        g = {}

        def dfs(node):
            if not node:
                return None
            if node in g:
                return g[node]

            cloned = Node(node.val)
            g[node] = cloned
            for nei in node.neighbors:
                cloned.neighbors.append(dfs(nei))

            return cloned

        return dfs(node)
