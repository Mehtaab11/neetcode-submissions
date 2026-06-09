class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # A tree with n nodes must have exactly n - 1 edges.
        # If not, it is either disconnected or contains a cycle.
        if len(edges) != n - 1:
            return False

        # Initially, every node is its own parent
        parent = list(range(n))

        # rank[i] stores the size of the tree rooted at i
        rank = [1] * n

        def find(x):
            # Find the root of x
            # Path compression makes future finds faster
            if x != parent[x]:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a, b):
            # Find roots of both nodes
            rootA = find(a)
            rootB = find(b)

            # If both nodes already have the same root,
            # adding this edge creates a cycle
            if rootA == rootB:
                return False

            # Union by rank (size):
            # attach the smaller tree to the larger tree
            if rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
                rank[rootA] += rank[rootB]
            else:
                parent[rootA] = rootB
                rank[rootB] += rank[rootA]

            return True

        # Process each edge
        for u, v in edges:

            # If union fails, a cycle exists
            if not union(u, v):
                return False

        # No cycles found and edge count is n - 1,
        # therefore the graph is a valid tree
        return True