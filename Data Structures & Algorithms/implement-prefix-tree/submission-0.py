class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        self._total = 0

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
            node.count += 1
        node.is_end = True
        self._total += 1

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return False if node.count == 0 else True