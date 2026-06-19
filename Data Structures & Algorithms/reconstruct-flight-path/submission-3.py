class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {src: [] for src, dst in tickets}

        tickets.sort()

        for src, dst in tickets:
            graph[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in graph:
                return False

            for i, v in enumerate(graph[src]):
                graph[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                graph[src].insert(i, v)
                res.pop()

        dfs("JFK")
        return res
