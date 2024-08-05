import io
from typing import List
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = set()
        nonDistinct = set()
        
        for s in arr:
            if s not in nonDistinct:
                if s in distinct:
                    distinct.remove(s)
                    nonDistinct.add(s)
                else:
                    distinct.add(s)
        
        if len(distinct) < k:
            return ""
        
        for s in arr:
            if s in distinct:
                k -= 1
                if k == 0:
                    return s
        
        return ""

obj = Solution()
#data = obj.kthDistinct(arr = ["d","b","c","b","c","a"], k = 2)
#data = obj.kthDistinct(arr = ["aaa","aa","a"], k = 1)
data = obj.kthDistinct(arr = ["a","b","a"], k = 3)
print(data)