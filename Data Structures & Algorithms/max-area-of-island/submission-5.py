class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = 0
        visited = set()

        def inbound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        # def dfs(r, c):
        #     if not inbound(r, c) or grid[r][c] != 1 or (r,c) in visited:
        #         return 0
        #     visited.add((r, c))
        #     curr_area = 1

        #     for dr, dc in dir:
        #         curr_area += dfs(r + dr, c + dc)

        #     return curr_area

        def dfs(r, c):
            queue = [(r,c)]
            curr_area = 0

            while queue:
                r,c = queue.pop()

                if (r,c) in visited or grid[r][c]==0:
                    continue
                
                visited.add((r,c))
                curr_area += 1

                for dr, dc in dir:
                    if inbound(r+dr, c+dc):
                        queue.append((r+dr, c+dc))

            return curr_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(dfs(r, c), area)

        return area
