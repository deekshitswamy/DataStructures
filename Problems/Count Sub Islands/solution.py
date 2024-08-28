import io
from typing import List
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row_limit = len(grid2)
        col_limit = len(grid2[0])
        
        def traveller(i, j):
            if i < 0 or j < 0 or i >= row_limit or j >= col_limit or grid2[i][j] == 0:
                return
            if grid1[i][j] != 1:
                nonlocal flag
                flag = False
            grid2[i][j] = 0  # Mark cell as visited
            traveller(i + 1, j)
            traveller(i - 1, j)
            traveller(i, j + 1)
            traveller(i, j - 1)
        
        count = 0
        for i in range(row_limit):
            for j in range(col_limit):
                if grid2[i][j] == 1:
                    flag = True
                    traveller(i, j)
                    if flag:
                        count += 1
        
        return count

obj = Solution()
#data = obj.countSubIslands(grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])
data = obj.countSubIslands(grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]])
print(data)