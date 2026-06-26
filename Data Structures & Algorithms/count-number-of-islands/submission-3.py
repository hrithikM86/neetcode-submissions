class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        def in_bound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c):  # Visit and mark nodes, nothing else
            if not in_bound(r, c) or (r, c) in visited or grid[r][c] == '0':
                return

            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    count += 1

        return count