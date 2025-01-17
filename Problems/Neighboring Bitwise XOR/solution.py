import io
from typing import List
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        a = 0
        for i in derived:
            a = a ^ i
        if not(a):
            return True
        return False

obj = Solution()
#data = obj.doesValidArrayExist(derived = [1,1,0])
#data = obj.doesValidArrayExist(derived = [1,1])
data = obj.doesValidArrayExist(derived = [1,0])
print(data)