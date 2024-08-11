import math
from typing import List


class Arrays:
    def pascals_triangle(self, numRows: int) -> List[List[int]]:
        def ncr(n: int, r: int):
            ncr_val = math.factorial(
                n) // (math.factorial(n-r) * math.factorial(r))
            return ncr_val

        result = [[1]]
        if numRows == 1:
            return result
        for i in range(2, numRows):
            temp_result = []
            for j in range(i+1):
                temp_result.append(ncr(i, j))
            result.append(temp_result)
        return result

    def majority_element(self, nums: List[int]) -> List[int]:
        d = {}
        result = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d:
            if d[i] > len(nums) // 3:
                result.append(i)
        return result

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            temp_result = [nums[i]]
            for j in range(len(nums)):
                if i != j:
                    temp_result.append(nums[j])
                    if len(temp_result) == 3 and sum(temp_result) == 0:
                        result.append(temp_result)
                        temp_result = [nums[i]]

        res = []
        [res.append(x) for x in result if x not in res]
        return res


arr = [1, -1, -1, 0]
print("\nThe Result is : ", Arrays().three_sum(arr))
