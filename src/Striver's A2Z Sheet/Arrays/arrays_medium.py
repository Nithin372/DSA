import math
from typing import List


class Arrays:
    def two_sum_problem(self, n: int, arr: List[int], target: int) -> str:
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] == target:
                    return 'YES'
        return 'NO'

    def sort_0_1_2(self, nums: List[int]) -> List[int]:

        def partition(nums, low, high):
            pivot = nums[low]
            i = low + 1
            j = high

            while True:
                while i <= j and nums[i] <= pivot:
                    i += 1
                while i <= j and nums[j] > pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    break

            nums[low], nums[j] = nums[j], nums[low]
            return j

        def quick_sort(nums, low, high):
            if low < high:
                pivot = partition(nums, low, high)
                quick_sort(nums, low, pivot - 1)
                quick_sort(nums, pivot + 1, high)

        quick_sort(nums, 0, len(nums) - 1)
        return nums

    def max_sub_array_sum(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        sum = 0
        for i in range(n):
            sum += nums[i]
            max_sum = max(max_sum, sum)
            if sum < 0:
                sum = 0
        return max_sum

    def kadanes_algorithm(self, nums: list[int]) -> list[int]:
        n = len(nums)
        max_sum = 0
        sub_arr = []
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                if sum > max_sum:
                    max_sum = sum
                    sub_arr = nums[i:j+1]
        return sub_arr

    def stock_buy_sell(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

    def next_permutation(self, nums: List[int]) -> None:
        ind = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                ind = i - 1
                break
        for i in range(len(nums)-1, ind, -1):
            if nums[i] > nums[ind]:
                (nums[i], nums[ind]) = (nums[ind], nums[i])
                break
        nums[ind+1:] = sorted(nums[ind+1:])
        if ind == -1:
            nums.sort()

    def leader_arr(self, nums: List[int]) -> List[int]:
        leaders = []
        for i in range(len(nums)-1):
            j = i + 1
            while nums[j] < nums[i]:
                if j == len(nums)-1:
                    leaders.append(nums[i])
                    break
                j += 1
        leaders.append(nums[len(nums)-1])
        return leaders

    def len_longest_consecutive_seq(self, nums: List[int]) -> int:
        max_sum = 0
        for i in nums:
            sum = 0
            while True:
                if i+1 in nums:
                    sum += 1
                    i += 1
                else:
                    break
            max_sum = max(max_sum, sum)

        return max_sum+1

    def set_zeroes(self, matrix: List[List[int]]) -> List[List[int]]:
        row = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.append([i, j])
        for i in row:
            matrix[i[0]] = [0] * len(matrix[0])
            for j in range(len(matrix)):
                matrix[j][i[1]] = 0
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])
        result = [[0 for _ in range(columns)] for _ in range(rows)]

        for i in range(rows):
            j = columns-1-i
            k = 0
            while k < rows:
                result[k][j] = matrix[i][k]

                k += 1
        print(result)

    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        columns = len(matrix[0])
        result = []
        top = 0
        bottom = rows - 1
        left = 0
        right = columns-1

        while top <= bottom and left <= right:
            # Moving Left to Right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            # Moving top to Bottom
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            # Moving Right to Left
            if top <= bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            # Moving Bottom to up
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result

    def subarray_sum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count


arr = [1, 2, 3]
print("\nThe Result is : ", Arrays().subarray_sum(arr, 3))
