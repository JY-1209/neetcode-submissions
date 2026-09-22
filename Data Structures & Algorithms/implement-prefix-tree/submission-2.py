class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        if not word:
            return

        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                new_node = TreeNode()
                cur_node.children[char] = new_node
            
            cur_node = cur_node.children[char]

        cur_node.is_word = True


    def search(self, word: str) -> bool:
        cur_node = self.root

        for c in word:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]

        return cur_node.is_word

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root

        for c in prefix:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
        
        return True

        
        