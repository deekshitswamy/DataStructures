import io
from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_value=max(candies)

        def candies_distribution_possible(needed_piles):
            total_piles=0
            for candie in candies:
                total_piles+=(candie//needed_piles)
            
            return True if total_piles>=k else False

        def binary_search(max_value):
            l=1
            r=max_value
            max_candies=0
            while l<=r:
                
                mid=(r-l)//2+l

                if mid>0 and candies_distribution_possible(mid):
                    max_candies=mid
                    l=mid+1

                else:
                    r=mid-1


            return max_candies
        
        return binary_search(max_value)

obj = Solution()
#data = obj.maximumCandies(candies = [5,8,6], k = 3)
data = obj.maximumCandies(candies = [2,5], k = 11)
print(data)