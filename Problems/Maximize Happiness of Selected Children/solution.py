import io
from typing import List
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        selected=0
        sum_happiness_value=0
        for happiness_value in happiness:
            if selected==k:
                return sum_happiness_value
            sum_happiness_value+=max(0,happiness_value-selected)
            selected+=1
      
        return  sum_happiness_value

obj = Solution()
#data = obj.maximumHappinessSum(happiness = [1,2,3], k = 2)
#data = obj.maximumHappinessSum(happiness = [1,1,1,1], k = 2)
data = obj.maximumHappinessSum(happiness = [2,3,4,5], k = 1)
print(data)