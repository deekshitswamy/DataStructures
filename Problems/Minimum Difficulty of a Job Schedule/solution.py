import io
import math
from typing import List
from functools import cache
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def helper(job_i, day, curr_difficulty):
            ## We ever start doing jobs after the max day
            if day > d:
                return math.inf
            if job_i == len(jobDifficulty):
                if day == d:
                    ## All jobs complete and the last job on the final day
                    ## This algorithm also implies then that all preceding days have a job
                    return curr_difficulty
                else:
                    ## We did not finish with each day having a job 
                    return math.inf

            ## We to this job on the current day
            a = helper(job_i+1, day, max(curr_difficulty, jobDifficulty[job_i]))

            ## We to this job on the next day
            b = helper(job_i+1, day+1, jobDifficulty[job_i]) + curr_difficulty

            return min(a, b)

        if len(jobDifficulty) < d:
            return -1
        return helper(1, 1, jobDifficulty[0])

obj = Solution()
#data = obj.minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2)
#data = obj.minDifficulty(jobDifficulty = [9,9,9], d = 4)
data = obj.minDifficulty(jobDifficulty = [1,1,1], d = 3)
print(data)