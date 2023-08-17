import io
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        m=len(mat[0])
        ans=[]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    ans.append((i,j))

                else:
                    mat[i][j]="#"

        for row,col in ans:
            for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                new_row=row+dx
                new_col=col+dy
                if 0<=new_row<n and 0<=new_col<m and mat[new_row][new_col]=="#":
                    mat[new_row][new_col]=mat[row][col]+1
                    ans.append((new_row,new_col))

        return mat


obj = Solution()
data = obj.updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]])
#data = obj.updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]])
print(data)