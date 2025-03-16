import io
from math import sqrt
from typing import List
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def repairCount(time):
            count = 0
            for r in ranks:
                count += int(sqrt(time / r))
            return count
        
        l = 1
        r = ranks[0] * cars * cars
        res = -1
        while l <= r:
            m = (l + r) // 2
            repaired = repairCount(m)
            if repaired >= cars:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

obj = Solution()
#data = obj.repairCars(ranks = [4,2,3,1], cars = 10)
data = obj.repairCars(ranks = [5,1,8], cars = 6)
print(data)