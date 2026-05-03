class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid) {
        const explore = (grid, r, c, visited) => {
            if (!(0 <= r && r < grid.length)) return 0;
            if (!(0 <= c && c < grid[0].length)) return 0;

            if ( grid[r][c] === 0) return 0;
            const pos = r + "," + c;

            if (visited.has(pos)) return 0;
            visited.add(pos);

            let size = 1

            size += explore(grid, r - 1, c, visited);
            size += explore(grid, r + 1, c, visited);
            size += explore(grid, r, c - 1, visited);
            size += explore(grid, r, c + 1, visited);

            return size;
        };

        let maximum = 0;
        const visited = new Set();
        for (let r = 0; r < grid.length; r++) {
            for (let c = 0; c < grid[0].length; c++) {
                let currentArea = explore(grid, r, c, visited);
                if (currentArea > maximum) {
                    maximum = currentArea;
                }
            }
        }

        return maximum;
    }
}
