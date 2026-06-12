class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n
        components = n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            if size[rootA] < size[rootB]:
                parent[rootA] = rootB
                size[rootB] += size[rootA]
            else:
                parent[rootB] = rootA
                size[rootA] += size[rootB]
            return True

        for u, v in edges:
            if union(u, v):
                components -= 1

        return components
