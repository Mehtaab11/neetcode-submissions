class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        nei = collections.defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        q = deque([beginWord])
        visited = set([beginWord])

        ans = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return ans

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]

                    for curr in nei[pattern]:
                        if curr not in visited:
                            visited.add(curr)
                            q.append(curr)
            ans += 1

        return 0
