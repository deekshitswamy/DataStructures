import io
from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def isPossible(val , position , m):
            count = 1
            curr_pos = position[0]
            for i in range(1 , len(position)):
                if position[i]-curr_pos>=val:
                    count+=1
                    curr_pos = position[i]
            if count>=m:
                return True

            return False
        
        position.sort()
        low = 1
        high = max(position)-min(position)
        ans = -1
        while low<=high:
            mid = low + (high-low)//2
            if isPossible(mid , position , m):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans

obj = Solution()
#data = obj.maxDistance(position = [1,2,3,4,7], m = 3)
data = obj.maxDistance(position = [5,4,3,2,1,1000000000], m = 2)
print(data)