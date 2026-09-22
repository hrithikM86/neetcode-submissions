class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = 0
        visited = set()

        def inbound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c, visited):
            if not inbound(r, c) or grid[r][c] != 1 or (r, c) in visited:
                return 0
            visited.add((r, c))
            curr_area = 1

            for dr, dc in dir:
                curr_area += dfs(r + dr, c + dc, visited)

            return curr_area

        for r in range(ROWS):
            for c in range(COLS):
                if inbound(r, c) and grid[r][c] == 1 and (r, c) not in visited:
                    area = max(dfs(r, c, visited), area)

        return area
