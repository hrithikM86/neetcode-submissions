class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < columns
    
        def dfs(r, c, visited):
            if not in_bounds(r, c) or (r, c) in visited or grid[r][c] == '0':
                return
            
            visited.add((r,c))

            for x, y in directions:
                dfs(r+x, c+y, visited)

        rows, columns = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        count = 0
        visited = set()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r, c, visited)
                    count+=1
        return count


        


        