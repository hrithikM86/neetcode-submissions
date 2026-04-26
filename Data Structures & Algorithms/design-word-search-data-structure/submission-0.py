class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        self._total = 0
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
            node.count =+ 1
        node.is_end = True
        self._total += 1
        

    def search(self, word: str) -> bool:
        return self._dfs(self.root, 0, word)

    def _dfs(self, node, index, word):
        if len(word) == index:
            return node.is_end

        char = word[index]

        if char == '.':
            for child in node.children.values():
                if self._dfs(child, index+1, word):
                    return True    
            return False
        else:
            if char not in node.children:
                return False
            return self._dfs(node.children[char], index+1, word)



            

        
