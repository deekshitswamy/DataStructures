import io
from typing import List
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        left = left+1 if left ==1 else left

        primes=[True]*(right+1)

        p=2
        prev = -1
        diff = float('inf')
        res=[-1,-1]
        while p*p <= right:
            if(primes[p]==True):
                for i in range(p * p, right+1, p):
                    primes[i] = False
            p+=1
        
        for p in range(left,len(primes)):
            if primes[p]:
                if prev==-1:
                    prev = p
                    continue
                if diff> p-prev:
                    res=[prev,p]
                    diff = p-prev
                if diff == 2:
                    return res
                prev = p

        return res

obj = Solution()
#data = obj.closestPrimes(left = 10, right = 19)
data = obj.closestPrimes(left = 4, right = 6)
print(data)