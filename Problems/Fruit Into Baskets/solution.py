import io
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int)
        maxval = 0
        l = 0
        for fruit in fruits:
            dic[fruit] += 1
            while len(dic) > 2:
                subfruit = fruits[l]
                dic[subfruit] -= 1
                if dic[subfruit] == 0:
                    del dic[subfruit]
                l += 1
            
            current = 0
            for key in dic.keys():
                current += dic[key]
            maxval = max(maxval, current)
        return maxval

obj = Solution()
#data = obj.totalFruit(fruits = [1,2,1])
#data = obj.totalFruit(fruits = [0,1,2,2])
data = obj.totalFruit(fruits = [1,2,3,2,2])
print(data)