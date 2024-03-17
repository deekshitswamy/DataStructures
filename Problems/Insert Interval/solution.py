import io
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lst  = []
        lst.extend(intervals)
        lst.append(newInterval)
        lst.sort(key = lambda x : (x[0], x[1]))
        print(lst)
        ans = []
        if not lst:
            return []
        else:
            x, y = lst[0]
            for i in range(len(lst)):
                n_x, n_y = lst[i]
                if y < n_x:
                    ans.append([x, y])
                    x = n_x
                    y = n_y
                else:
                    y = max(y, n_y)
        ans.append([x, y])
        return ans

obj = Solution()
#data = obj.insert(intervals = [[1,3],[6,9]], newInterval = [2,5])
data = obj.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])
print(data)