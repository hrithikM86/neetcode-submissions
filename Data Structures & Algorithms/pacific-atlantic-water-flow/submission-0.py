from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        visited_p = set()
        visited_a = set()

        def inbound(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c, visited):
            if not inbound(r,c) or (r,c) in visited:
                return

            visited.add((r,c))

            for dr, dc in dirs:
                r1, c1 = r + dr, c + dc
                if inbound(r1, c1) and (r1, c1) not in visited and heights[r][c] <= heights[r1][c1]:
                    dfs(r1, c1, visited)

        for r in range(ROWS):
            dfs(r,0,visited_p)
            dfs(r, COLS-1, visited_a)
        
        for c in range(COLS):
            dfs(0,c,visited_p)
            dfs(ROWS-1, c, visited_a)

        res = []
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visited_p and (r,c) in visited_a:
                    res.append([r,c])
        return res
                


            


            




