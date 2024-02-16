import io
from typing import List
from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)
        frequencies = list(freq_map.values())
        frequencies.sort()

        elements_removed = 0
        for i in range(len(frequencies)):
            elements_removed += frequencies[i]
            if elements_removed > k:
                return len(frequencies) - i
        return 0

obj = Solution()
#data = obj.findLeastNumOfUniqueInts(arr = [5,5,4], k = 1)
data = obj.findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3)
print(data)