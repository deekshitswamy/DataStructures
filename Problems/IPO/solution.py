import io
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit=[]
        min_capital=[(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(min_capital) 
        for i in range(k):
            while min_capital and min_capital[0][0]<=w:
                c,p=heapq.heappop(min_capital) 
                heapq.heappush(max_profit,-1*p)
            if not max_profit:
                break
            w+=-1*heapq.heappop(max_profit)
        return w

obj = Solution()
#data = obj.findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1])
data = obj.findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2])
print(data)