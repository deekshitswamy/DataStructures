import io
from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        sorted_worker=sorted(worker)
        jobs=zip(difficulty,profit)
        sorted_jobs=sorted(jobs)
        n=len(sorted_jobs)
        best_profit=0
        total_best_profit=0
        i=0
        for skill in sorted_worker:
            while i<n and skill>=sorted_jobs[i][0]:
                best_profit=max(best_profit, sorted_jobs[i][1])
                i+=1
            total_best_profit+=best_profit
        return total_best_profit

obj = Solution()
#data = obj.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7])
data = obj.maxProfitAssignment(difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25])
print(data)