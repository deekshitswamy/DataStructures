import io
from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total=0
        for i,x in enumerate(tickets):
            if i<=k:
                total+=min(tickets[i],tickets[k])
                
            else:
                total+=min(tickets[i],tickets[k]-1)
                
        return total

obj = Solution()
#data = obj.timeRequiredToBuy(tickets = [2,3,2], k = 2)
data = obj.timeRequiredToBuy(tickets = [5,1,1,1], k = 0)
print(data)