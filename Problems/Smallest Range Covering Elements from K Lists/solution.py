from heapq import heappop, heappush
import io
from typing import List
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        pq = []
        ma = 0
        
        for i in range(n):
            heappush(pq, (nums[i][0] , i, 0))
            ma = max(ma , nums[i][0])
        
        ans = [pq[0][0] , ma]
        while True:
            _,i,j = heappop(pq)

            if j == len(nums[i])-1:
                break
                
            next_num = nums[i][j+1]
            ma = max( ma , next_num)
            heappush(pq,(next_num, i , j+1))
            
            if ma-pq[0][0] < ans[1] - ans[0]:
                ans= [pq[0][0], ma]
        return ans

obj = Solution()
#data = obj.smallestRange(nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])
data = obj.smallestRange(nums = [[1,2,3],[1,2,3],[1,2,3]])
print(data)