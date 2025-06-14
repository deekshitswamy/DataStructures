import io
from typing import List
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_arr = list(str(num))
        num_s = 0
        for i in range(len(num_arr)):
            if num_arr[i] != "9":
                num_s = num_arr[i]
                break
        for i in range(len(num_arr)):
            if num_arr[i] == num_s:
                num_arr[i] = "9"

        max_num = int("".join(num_arr))
        num_arr = list(str(num))
        num_s = num_arr[0]
        for j in range(len(num_arr)):
            if num_arr[j] == num_s:
                num_arr[j] = "0"

        min_num = int("".join(num_arr))
        return max_num - min_num

obj = Solution()
#data = obj.minMaxDifference(num = 11891)
data = obj.minMaxDifference(num = 90)
print(data)