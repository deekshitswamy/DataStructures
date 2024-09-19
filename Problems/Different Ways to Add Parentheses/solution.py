import io
import re
from typing import List
from itertools import product
from operator import add, sub, mul
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def cross_product(l1: list[int], l2: list[int], operator: str) -> list:
            op_map = {'+': add, '-': sub, '*': mul}
            op_func = op_map.get(operator, mul)  # Default to multiplication if operator is invalid
            return [op_func(i, j) for i, j in product(l1, l2)]          
                            
        nums = []
        operators = [c for c in expression if c in '+-*']
        nums = re.split(r'[+\-*]', expression)
        num_list = [int(n) for n in nums]
        n = len(num_list)
        dp = [[1 for i in range(n+1)] for _ in range(n)]
        # dp[i][j]: a list of all possible values, start from i, length = j
        for i in range(n):
            dp[i][1] = [num_list[i]]
        for j in range(2,n+1):
            for i in range( n+1-j):
                t = []
                for k in range(1, j): # idea is similar to calculate Catalan number
                    x = dp[i][k]
                    y = dp[i+k][j-k]
                    x = [x] if type(x) == int else x
                    y = [y] if type(y) == int else y
                    t = t + cross_product(x, y, operators[i+k-1])
                dp[i][j] = t
                
        return dp[0][n]

obj = Solution()
#data = obj.diffWaysToCompute(expression = "2-1-1")
data = obj.diffWaysToCompute(expression = "2*3-4*5")
print(data)