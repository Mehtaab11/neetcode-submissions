class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                components +=1

        return components