class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()

        ROWS = len(grid)
        COLS = len(grid[0])
        cnt = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))    
                elif grid[r][c] == 1:
                    cnt += 1

        time = 0
        while q and cnt > 0:

            q_len = len(q)

            for _ in range(q_len):
                r,c = q.popleft()

                for dr,dc in directions:
                    nr , nc = dr + r , dc + c

                    if 0 <= nr < ROWS and  0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        cnt -= 1
            
            time += 1
        
        return -1 if cnt > 0 else time