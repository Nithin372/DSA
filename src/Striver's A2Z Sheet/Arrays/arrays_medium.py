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

    def max_sub_array_sum(self, nums: List[int]) -> List[int]:
        pass


print("\nThe Result is : ", Arrays().sort_0_1_2([2, 0, 2, 1, 1, 0]))
