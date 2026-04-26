class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])

        def dfs(r, c, idx):
            if len(word) == idx:
                return True

            if r < 0 or r >= rows or c < 0 or c >= columns:
                return False
            if board[r][c] != word[idx]:
                return False
            if board[r][c] == '#':
                return False

            temp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r+1, c, idx+1) or
                dfs(r-1, c, idx+1) or
                dfs(r, c+1, idx+1) or
                dfs(r, c-1, idx+1)
                )

            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(columns):
                if dfs(r,c,0):
                    return True
        return False

        