class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = [i for i in range(0, n + 1)]

        # size array should be n + 1 
        # because question ask for 1 based indexing
        size = [1] * (n + 1)
        poss = []
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
            if union(u, v) == False:
                poss.append([u, v])

        return poss[-1]
