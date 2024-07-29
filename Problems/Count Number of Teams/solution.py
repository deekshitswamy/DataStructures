import io
from typing import List
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        for j in range(n):
            left_smaller = left_larger = right_smaller = right_larger = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_larger += 1
            
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                elif rating[k] > rating[j]:
                    right_larger += 1
            
            count += left_smaller * right_larger + left_larger * right_smaller
        
        return count

obj = Solution()
#data = obj.numTeams(rating = [2,5,3,4,1])
#data = obj.numTeams(rating = [2,1,3])
data = obj.numTeams(rating = [1,2,3,4])
print(data)