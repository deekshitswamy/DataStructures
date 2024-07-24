import io
from typing import List
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mySort(ele):
            s = str(ele)
            num = 0
            for c in s:
                num = 10*num + (mapping[ord(c) - ord('0')])
            return num
        
        return sorted(nums, key = mySort)

obj = Solution()
#data = obj.sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38])
data = obj.sortJumbled(mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123])
print(data)