class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = 0
        # visited = set()

        def inbound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c):
            if not inbound(r, c) or grid[r][c] != 1:
                return 0
            # visited.add((r, c))
            grid[r][c] = 0
            curr_area = 1

            for dr, dc in dir:
                curr_area += dfs(r + dr, c + dc)

            return curr_area

        for r in range(ROWS):
            for c in range(COLS):
                if inbound(r, c) and grid[r][c] == 1:
                    area = max(dfs(r, c), area)

        return area
