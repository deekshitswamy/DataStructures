import io
from typing import List
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        result = 1
        min_prime_factors = self._sieveEratosthenes(max(nums) + 1)
        prime_factors_count = [self._countUniquePrimeFactors(num, min_prime_factors) for num in nums]
        
        left_bound = [-1] * n
        right_bound = [n] * n
        stack = []
        
        for i in reversed(range(n)):
            while stack and prime_factors_count[stack[-1]] <= prime_factors_count[i]:
                left_bound[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for i in range(n):
            while stack and prime_factors_count[stack[-1]] < prime_factors_count[i]:
                right_bound[stack.pop()] = i
            stack.append(i)
        
        num_with_indices = [(num, i) for i, num in enumerate(nums)]
        
        def mod_pow(base: int, exponent: int) -> int:
            if exponent == 0:
                return 1
            if exponent % 2 == 1:
                return base * mod_pow(base, exponent - 1) % MOD
            return mod_pow(base * base % MOD, exponent // 2)
        
        for num, idx in sorted(num_with_indices, key=lambda x: (-x[0], x[1])):
            range_count = (idx - left_bound[idx]) * (right_bound[idx] - idx)
            actual_count = min(range_count, k)
            k -= actual_count
            result *= mod_pow(num, actual_count)
            result %= MOD
        
        return result

    def _sieveEratosthenes(self, limit: int) -> List[int]:
        min_prime_factors = [i for i in range(limit + 1)]
        for i in range(2, int(limit**0.5) + 1):
            if min_prime_factors[i] == i:
                for j in range(i * i, limit + 1, i):
                    min_prime_factors[j] = min(min_prime_factors[j], i)
        return min_prime_factors

    def _countUniquePrimeFactors(self, num: int, min_prime_factors: List[int]) -> int:
        unique_primes = set()
        while num > 1:
            divisor = min_prime_factors[num]
            unique_primes.add(divisor)
            while num % divisor == 0:
                num //= divisor
        return len(unique_primes)

obj = Solution()
#data = obj.maximumScore(nums = [8,3,9,3,8], k = 2)
data = obj.maximumScore(nums = [19,12,14,6,10,18], k = 3)
print(data)