import io
from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = []
        final = []
        for val1, val2 in zip(names, heights):
            obj = (val2, val1)
            arr.append(obj)
        arr.sort(reverse=True)
        return [item[1] for item in arr]

obj = Solution()
#data = obj.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170])
data = obj.sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150])
print(data)