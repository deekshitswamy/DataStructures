import io
from typing import Counter, List
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        mp = Counter(target)
        mp2 = Counter(arr)
    
        return mp == mp2

obj = Solution()
#data = obj.canBeEqual(target = [1,2,3,4], arr = [2,4,1,3])
#data = obj.canBeEqual(target = [7], arr = [7])
data = obj.canBeEqual(target = [3,7,9], arr = [3,7,11])
print(data)