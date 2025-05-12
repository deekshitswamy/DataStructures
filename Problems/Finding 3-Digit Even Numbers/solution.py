import io
from typing import List
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counts = Counter(digits)
        res = []
        for x in range(1, 10):
            if counts[x] == 0:
                continue
            for y in range(10):
                if counts[y] == 0: 
                    continue
                if x == y and counts[y] < 2:
                    continue
                for z in range(0, 10, 2):
                    if counts[z] == 0: 
                        continue
                    if x == y == z and counts[z] < 3:
                        continue
                    if (x == z or y == z) and counts[z] < 2:
                        continue
                    num = x * 100 + y * 10 + z
                    res.append(num)
        
        return sorted(res)

obj = Solution()
#data = obj.findEvenNumbers(digits = [2,1,3,0])
#data = obj.findEvenNumbers(digits = [2,2,8,8,2])
data = obj.findEvenNumbers(digits = [3,7,5])
print(data)