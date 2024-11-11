import io
import math
from typing import List
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = self.sieve_of_eratosthenes(1000)
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]: continue
            
            target = nums[i] - nums[i + 1]
            prime = next((p for p in primes if p > target), None)
            if not prime: return False
            
            nums[i] -= prime
            if nums[i] <= 0: return False
        
        return True
    
    def sieve_of_eratosthenes(self, max_num):
        is_prime = [True] * (max_num + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.sqrt(max_num)) + 1):
            if is_prime[i]:
                for j in range(i * i, max_num + 1, i):
                    is_prime[j] = False
        return [i for i in range(2, max_num + 1) if is_prime[i]]

obj = Solution()
#data = obj.primeSubOperation(nums = [4,9,6,10])
#data = obj.primeSubOperation(nums = [6,8,11,12])
data = obj.primeSubOperation(nums = [5,8,3])
print(data)