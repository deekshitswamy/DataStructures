import io
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass

obj = Solution()
#data = obj.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
#data = obj.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
data = obj.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
print(data)