import io
from typing import List
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        arr.append(-1)
        curr_counter = 0
        last_v = -1
        for v in arr:
            if v != last_v:
                if curr_counter * 4 > n:
                    return last_v
                curr_counter = 1
                last_v = v
            else:
                curr_counter += 1
        return None

obj = Solution()
#data = obj.findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10])
data = obj.findSpecialInteger(arr = [1,1])
print(data)