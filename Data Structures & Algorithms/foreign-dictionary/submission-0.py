class Solution:
    def topo(self, adj):
        n = len(adj)
        indegree = {ch: 0 for ch in adj}

        for node in adj:
            for nei in adj[node]:
                indegree[nei] += 1

        q = collections.deque()
        for node in indegree:
            if indegree[node] == 0:
                q.append(node)

        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) != len(adj):
            return ""
        return "".join(res)

    def foreignDictionary(self, words: List[str]) -> str:

        adj = {ch: set() for w in words for ch in w}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            minLen = min(len(w1), len(w2))

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        return self.topo(adj)
