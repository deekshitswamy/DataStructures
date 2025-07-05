import io
from typing import List
from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        luckyNum = -1

        for key, value in freq.items():
            if key == value:
                luckyNum = max(luckyNum, key)

        return luckyNum

obj = Solution()
#data = obj.findLucky(arr = [2,2,3,4])
#data = obj.findLucky(arr = [1,2,2,3,3,3])
data = obj.findLucky(arr = [2,2,2,3,3])
print(data)