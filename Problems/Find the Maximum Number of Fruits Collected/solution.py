import io
from typing import List
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n, total = len(fruits), 0 

        for i in range(n):
            for j in range(n):
                if i == j:
                    total += fruits[i][j]
                    fruits[i][j] = 0 

        @lru_cache(None)
        def function(i,j,k):
            if i >= n or i < 0 or j >= n or i-j <= 0 or k <= 0:
                return 0 
            return fruits[i][j] + max(function(i-1,j+1,k),function(i,j+1,k),function(i+1,j+1,k))
        
        @lru_cache(None)
        def kunction(i,j,k):
            if i >= n or j >= n or j < 0 or i-j >= 0 or k <= 0:
                return 0 
            return fruits[i][j] + max(kunction(i+1,j-1,k),kunction(i+1,j,k),kunction(i+1,j+1,k))

        return total + function(n-1,0,n-1) + kunction(0,n-1,n-1)

obj = Solution()
#data = obj.maxCollectedFruits(fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]])
data = obj.maxCollectedFruits(fruits = [[1,1],[1,1]])
print(data)