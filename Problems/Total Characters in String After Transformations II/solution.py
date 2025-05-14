import io
from typing import List
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = 26

        initial_counts = [0] * n
        for char in s:
            initial_counts[ord(char) - ord('a')] += 1

        transformation_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            transform_length = nums[i]
            for k in range(1, transform_length + 1):
                next_index = (i + k) % n
                transformation_matrix[next_index][i] = 1

        def multiply_matrices(A, B):
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def power(matrix, p):
            result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            while p > 0:
                if p % 2 == 1:
                    result = multiply_matrices(result, matrix)
                matrix = multiply_matrices(matrix, matrix)
                p //= 2
            return result

        final_transformation_matrix = power(transformation_matrix, t)

        final_counts = [0] * n
        for i in range(n):
            for j in range(n):
                final_counts[i] = (final_counts[i] + final_transformation_matrix[i][j] * initial_counts[j]) % MOD

        total_length = sum(final_counts) % MOD
        return total_length

obj = Solution()
#data = obj.lengthAfterTransformations(s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
data = obj.lengthAfterTransformations(s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
print(data)