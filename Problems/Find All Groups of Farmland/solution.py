import io
from typing import List
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n=len(land)
        m=len(land[0])
        ans=[]
        for i in range(n):
            for j in range(m):
                if land[i][j]:
                    min_i,min_j=i,j
                    max_i,max_j=i,j
                    stack=[(i,j)]
                    land[i][j]=0
                    while stack:
                        i,j=stack.pop()
                        for x,y in (i-1,j),(i,j-1),(i,j+1),(i+1,j):
                            if 0<=x<n and 0<=y<m and land[x][y]:
                                stack.append((x,y))
                                land[x][y]=0
                                max_i=max(max_i,x)
                                max_j=max(max_j,y)
                    ans.append([min_i,min_j,max_i,max_j])
        return ans

obj = Solution()
#data = obj.findFarmland(land = [[1,0,0],[0,1,1],[0,1,1]])
#data = obj.findFarmland(land = [[1,1],[1,1]])
data = obj.findFarmland(land = [[0]])
print(data)