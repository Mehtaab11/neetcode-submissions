class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def addroom(r, c):
            if (
                r < 0
                or c < 0
                or r == rows
                or c == cols
                or (r, c) in visited
                or grid[r][c] != 2147483647
                # current elem should be land
            ):
                return

            visited.add((r, c))
            q.append((r, c))

        # most important so that we start traversing only at treasure
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))

        dist = 0
        while q:
            # Run the loop for one level
            # add all the next rooms for all the elems
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addroom(r + 1, c)
                addroom(r - 1, c)
                addroom(r, c - 1)
                addroom(r, c + 1)

            # After we are done with the level we will be moving to the next level
            # Which can then be incremented by 1
            dist += 1
