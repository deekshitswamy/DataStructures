import io
import math
from typing import List
from heapq import heappop, heappush
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        hp=[]
        maxx=-math.inf
        min_range=math.inf
        for i in range(n):
            # we push the value, index in terms of nums and the sub index 
            heappush(hp,(nums[i][0],i,0))
            if maxx<nums[i][0]:
                maxx=nums[i][0]
        res=[math.inf, -math.inf]
        while hp:
            min_val,idx,sub_idx=heappop(hp)
            if maxx-min_val<min_range:
                min_range=maxx-min_val
                res=[maxx,min_val]
            if sub_idx+1<len(nums[idx]):
                heappush(hp,(nums[idx][sub_idx+1],idx,sub_idx+1))
                if maxx<nums[idx][sub_idx+1]:
                    maxx=nums[idx][sub_idx+1]
            else:
                break
        return res

obj = Solution()
#data = obj.smallestRange(nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])
data = obj.smallestRange(nums = [[1,2,3],[1,2,3],[1,2,3]])
print(data)