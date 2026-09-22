class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, k):
            if not board or i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return False

            if board[i][j] != word[k]:
                return False
            elif k >= len(word) - 1:
                return True

            temp = board[i][j]
            board[i][j] = '#'
            
            res = (dfs(i + 1, j, k+1) or dfs(i - 1, j, k+1)
                    or dfs(i, j + 1, k+1) or dfs(i, j - 1, k+1))
                
            board[i][j] = temp
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):

                if dfs(i, j, 0):
                    return True
        return False