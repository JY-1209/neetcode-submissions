class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        
        def dfs(word_idx, row, col):
            if word_idx == len(word):
                return True

            if word_idx >= len(word) or row >= len(board) or col >= len(board[0]) or word[word_idx] != board[row][col] or min(row, col) < 0 or (row, col) in path:
                return False
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            path.add((row, col))
            for direction in directions:
                new_row, new_col = (row + direction[0], col + direction[1])

                if new_row < len(board) and new_col < len(board[0]):
                    if dfs(word_idx + 1, new_row, new_col):
                        return True
            path.remove((row, col))
            return False
            
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(0, r, c):
                    return True
        
        return False