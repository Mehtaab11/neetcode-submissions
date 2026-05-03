class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    orangesRotting(grid) {
        const queue = [];
        let fresh = 0;
        let time = 0;

        let rows = grid.length;
        let cols = grid[0].length;

        for (let r = 0; r < rows; r += 1) {
            for (let c = 0; c < cols; c += 1) {
                if (grid[r][c] === 2) {
                    queue.push([r, c]);
                } else if (grid[r][c] === 1) {
                    fresh++;
                }
            }
        }

        let directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ];

        while (queue.length > 0 && fresh > 0) {
            let size = queue.length;
            for (let i = 0; i < size; i++) {
                let [r, c] = queue.shift();

                for (let [dr, dc] of directions) {
                    let nr = r + dr;
                    let nc = c + dc;

                    if (nr < 0 || nr == rows || nc < 0 || nc == cols || grid[nr][nc] != 1) {
                        continue;
                    }

                    grid[nr][nc] = 2;
                    queue.push([nr, nc]);
                    fresh--;
                }
            }

            time++;
        }

        return fresh === 0 ? time : -1;
    }
    // find rotten fruit and start
    // number of bfs with count till we reach the last element
    // after traversal check the grid again if found any fresh (has 1 and unvisited fruit there) that means return -1 given
    // given in the question
}
