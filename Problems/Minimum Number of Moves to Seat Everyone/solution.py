import io
from typing import List
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n=len(seats)
        ans=0
        for i in range(n):
            ans+=abs(seats[i]-students[i])
        return ans

obj = Solution()
#data = obj.minMovesToSeat(seats = [3,1,5], students = [2,7,4])
#data = obj.minMovesToSeat(seats = [4,1,5,9], students = [1,3,2,6])
data = obj.minMovesToSeat(seats = [2,2,6,6], students = [1,3,2,6])
print(data)