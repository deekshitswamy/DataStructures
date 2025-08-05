import io
from typing import List
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c=0
        f=0
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    baskets.pop(j)
                    c=c+1
                    break
            if c==1:
                c=0
            else:
                f=f+1
                c=0
        return f

obj = Solution()
#data = obj.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4])
data = obj.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7])
print(data)