import io
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r=0,len(height)-1
        leftmax , rightmax =height[l],height[r]
        water=0
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax=max(leftmax,height[l])
                water+=leftmax-height[l]
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                water+=rightmax-height[r]
        return water

obj = Solution()
#data = obj.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])
data = obj.trap(height = [4,2,0,3,2,5])
print(data)