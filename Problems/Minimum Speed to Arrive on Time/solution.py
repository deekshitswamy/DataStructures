import io
from typing import List
from bisect import bisect_right
from math import ceil, modf
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        if sum(dist) <= hour:
            return 1

        mx = max(dist)
        last = dist.pop()
        dist.sort()

        def calc_time(speed):
            time = len(dist)
            end = len(dist)
            start = 0
            imag_speed = speed
            while start < len(dist):
                start = bisect_right(dist, imag_speed)
                time += end - start
                imag_speed += speed
            return time + last / speed

        l = 2
        r = mx if hour.is_integer() else max(mx, ceil(last / round(modf(hour)[0], 2)))
        while True:
            speed = (l + r) // 2
            if calc_time(speed) > hour:
                if calc_time(speed + 1) <= hour:
                    return speed + 1
                else:
                    l = speed + 1
            else:
                r = speed - 1
obj = Solution()
#data = obj.minSpeedOnTime(dist = [1,3,2], hour = 6)
#data = obj.minSpeedOnTime(dist = [1,3,2], hour = 2.7)
data = obj.minSpeedOnTime(dist = [1,3,2], hour = 1.9)
print(data)