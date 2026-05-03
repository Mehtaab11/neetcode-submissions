class Solution {
    numIslands(grid) {
        const explore = (grid, r, c, visited) => {
            if (!(0 <= r && r < grid.length)) return false;
            if (!(0 <= c && c < grid[0].length)) return false;

            const pos = r + "," + c;
            if (visited.has(pos)) return false;
            visited.add(pos);

            if (grid[r][c] === "0") return false;

            explore(grid, r - 1, c, visited);
            explore(grid, r + 1, c, visited);
            explore(grid, r, c - 1, visited);
            explore(grid, r, c + 1, visited);

            return true;
        };
        let count = 0;
        const visited = new Set();
        for (let r = 0; r < grid.length; r++) {
            for (let c = 0; c < grid[0].length; c++) {
                if (explore(grid, r, c, visited) == true) {
                    count += 1;
                }
            }
        }

        return count;
    }
}
