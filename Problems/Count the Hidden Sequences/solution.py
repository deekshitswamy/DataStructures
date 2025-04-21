import io
from typing import List
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_s = 0
        max_s = 0
        cur = 0
        for d in differences:
            cur += d
            if cur < min_s:
                min_s = cur
            if cur > max_s:
                max_s = cur
        
        low_bound = lower - min_s
        high_bound = upper - max_s
        
        if high_bound < low_bound:
            return 0
        return high_bound - low_bound + 1

obj = Solution()
#data = obj.numberOfArrays(differences = [1,-3,4], lower = 1, upper = 6)
#data = obj.numberOfArrays(differences = [3,-4,5,1,-2], lower = -4, upper = 5)
data = obj.numberOfArrays(differences = [4,-7,2], lower = 3, upper = 6)
print(data)