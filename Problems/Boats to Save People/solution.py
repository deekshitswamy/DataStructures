import io
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boats += 1
        return boats + int(l == r)

obj = Solution()
#data = obj.numRescueBoats(people = [1,2], limit = 3)
#data = obj.numRescueBoats(people = [3,2,2,1], limit = 3)
data = obj.numRescueBoats(people = [3,5,3,4], limit = 5)
print(data)