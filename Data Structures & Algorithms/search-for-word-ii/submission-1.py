# class TreeNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False
#         self.count = 0

# class Tire:
#     def __init__(self):
#         self.root = Treenode()
#         self._total = 0

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TreeNode()
#             node = node.children[char]
#             node.count +=1
#         node.is_end = True
#         self._total += 1

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
            # Step 1: Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = set()

        # Step 2: DFS + Trie traversal
        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children:
                return

            next_node = node.children[char]

            if next_node.word:
                result.add(next_node.word)

            board[r][c] = '#'  # mark visited

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)

            board[r][c] = char  # restore (backtrack)

        # Step 3: Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return list(result)

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         result = []
#         for word in words:
#             if self._findWords(board, word):
#                 result.append(word)
#         return result

#     def _findWords(self, board, word):
#         rows, columns = len(board), len(board[0])

#         def dfs(r, c, idx):
#             if len(word) == idx:
#                 return True
#             if (r < 0 or r >= rows) or (c < 0 or c >= columns):
#                 return False
#             if board[r][c] == '#':        
#                 return False
#             if board[r][c] != word[idx]:  
#                 return False

#             temp = board[r][c]
#             board[r][c] = '#'
#             found = (
#                 dfs(r+1, c, idx+1) or
#                 dfs(r-1, c, idx+1) or
#                 dfs(r, c-1, idx+1) or
#                 dfs(r, c+1, idx+1)
#             )
#             board[r][c] = temp
#             return found

#         for r in range(rows):
#             for c in range(columns):
#                 if dfs(r, c, 0):
#                     return True
#         return False





        