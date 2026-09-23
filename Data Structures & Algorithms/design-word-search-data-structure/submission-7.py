class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root

        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            
            cur_node = cur_node.children[char]
        
        cur_node.is_word = True
        

    def search(self, word: str) -> bool:
        def dfs(cur_node, idx):
            
            for new_idx in range(idx, len(word)):
                char = word[new_idx]

                if char == ".":
                    for child in cur_node.children.values():
                        if dfs(child, new_idx + 1):
                            return True
                    
                    return False

                if char not in cur_node.children:
                    return False
                
                cur_node = cur_node.children[char]
            
            return cur_node.is_word
        
        return dfs(self.root, 0)
                