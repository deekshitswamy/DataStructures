import io
import math
from typing import List
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def to_base_k(n, k):
            if n == 0:
                return '0'
            digits = []
            while n > 0:
                rem = n % k
                digits.append(str(rem) if rem < 10 else chr(ord('A') + rem - 10))
                n //= k
            return ''.join(reversed(digits))

        sm = 0
        for i in range(1, 10):
            hold = to_base_k(i, k)
            if str(hold) == str(hold)[::-1]:
                n -= 1
                sm += i
                if n == 0:
                    return sm
        ln = 2

        while n > 0:
            curln = math.ceil(ln / 2)
            lower = 1 * pow(10, curln - 1)
            upper = 9 * int('1' * curln)
            for i in range(lower, upper + 1):
                if ln % 2 == 0:
                    number = int(str(i) + str(i)[::-1])
                else:
                    number = int(str(i) + str(i)[:curln - 1][::-1])
                hold = to_base_k(number, k)
                if str(hold) == str(hold)[::-1]:
                    sm += number
                    n -= 1
                    if n == 0:
                        return sm
            ln += 1
        return sm

obj = Solution()
#data = obj.kMirror(k = 2, n = 5)
#data = obj.kMirror(k = 3, n = 7)
data = obj.kMirror(k = 7, n = 17)
print(data)