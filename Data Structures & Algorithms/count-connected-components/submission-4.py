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
            nonlocal components
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return

            if size[rootA] < size[rootB]:
                parent[rootA] = rootB
                size[rootB] += size[rootA]
                components -= 1
            else:
                parent[rootB] = rootA
                size[rootA] += size[rootB]
                components -= 1

        for u, v in edges:
            union(u, v)

        return components
