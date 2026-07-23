class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        root = self.trie

        for char in word:
            if char in root.children:
                root = root.children[char]
            else:
                root.children[char] = TrieNode()
                root = root.children[char]
        
        root.is_word=True
        
    def search(self, word: str) -> bool:

        def dfs(root, idx):
            if idx == len(word) and root.is_word == True:
                return True
            
            if idx >= len(word):
                return False

            if word[idx] == ".":
                for char, child in root.children.items():
                    res = dfs(child, idx + 1)

                    if res:
                        return True
                return False
            else:
                if word[idx] in root.children:
                    return dfs(root.children[word[idx]], idx + 1)
                else:
                    return False
        
        return dfs(self.trie, 0)