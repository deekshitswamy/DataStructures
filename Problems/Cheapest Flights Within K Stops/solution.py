import io
from typing import List
class Solution:
    #Bellman-Ford algorithm
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        a = [float('inf')] * n
        a[src] = 0

        for _ in range(k+1):
            tmp = a[:]
            update = False
            for i,j,p in flights:
                if a[j] > tmp[i]+p:
                    a[j] = tmp[i]+p
                    update = True

            if not update:
                break
        
        return a[dst] if a[dst] != float('inf') else -1

obj = Solution()
#data = obj.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1)
#data = obj.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1)
data = obj.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0)
print(data)