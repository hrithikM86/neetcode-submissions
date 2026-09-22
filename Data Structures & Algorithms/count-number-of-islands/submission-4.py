class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dir = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        count = 0

        def inbound(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS
        
        def dfs(r, c, visited):
            if not inbound(r,c) or (r,c) in visited or grid[r][c] == '0':
                return

            visited.add((r,c))

            for dr, dc in dir:
                dfs(r + dr, c + dc, visited)

        for r in range(ROWS):
            for c in range(COLS):
                if inbound(r,c) and grid[r][c]=='1' and (r,c) not in visited:
                    dfs(r,c, visited)
                    count+=1
        return count





        

    
        