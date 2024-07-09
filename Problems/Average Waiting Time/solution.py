import io
from typing import List
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        add_time = 0
        ans = 0
        if len(customers) == 0:
            return -1
            
        time = customers[0][0] + customers[0][1]
        for i in range(1, len(customers)):
            if time < customers[i][0]:
                time  = customers[i][0]
            time += customers[i][1]
            add_time = time-customers[i][0]
            ans += add_time

        ans+=customers[0][1]
        return ans/len(customers)

obj = Solution()
#data = obj.averageWaitingTime(customers = [[1,2],[2,5],[4,3]])
data = obj.averageWaitingTime(customers = [[5,2],[5,4],[10,3],[20,1]])
print(data)