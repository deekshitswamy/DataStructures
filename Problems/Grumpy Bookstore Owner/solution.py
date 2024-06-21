import io
from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(customers)
        ans=mx=tamp=0
        for i in range(n):
            if not grumpy[i]:
                ans+=customers[i]
                customers[i]=0
            else:
                tamp+=customers[i]
            if i>=minutes:
                tamp-=customers[i-minutes] 
            mx=max(mx,tamp)
        return ans+mx

obj = Solution()
#data = obj.maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3)
data = obj.maxSatisfied(customers = [1], grumpy = [0], minutes = 1)
print(data)