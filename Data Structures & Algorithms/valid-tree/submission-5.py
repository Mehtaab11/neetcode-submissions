class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        rank = [0] * n

        def find(x):
            if x == parent[x]:
                return x

            parent[x] = find(parent[x])

            return parent[x]

        def union(a, b):

            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootB] < rank[rootA]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] += 1

        for u, v in edges:
            if union(u, v) == False:
                return False

        return True
