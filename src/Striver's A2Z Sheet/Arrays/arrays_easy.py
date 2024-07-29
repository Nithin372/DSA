import math
from typing import List


class Arrays:
    def largest(self, n: int, arr: List[int]) -> int:
        largest_element = arr[0]
        for i in range(1, n):
            if arr[i] > largest_element:
                largest_element = arr[i]
        return largest_element

    def print2largest(self, n: int, arr: List[int]) -> int:
        if n < 2:
            return -1
        large = 0
        second_large = 0
        for i in range(n):
            if arr[i] > large:
                second_large = large
                large = arr[i]
            elif arr[i] > second_large and arr[i] != large:
                second_large = arr[i]
        return second_large

    def check(self, nums: List[int]) -> bool:
        rotate = 0
        count = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1] and i < len(nums)-1:
                rotate = nums[i-1]
                nums = nums[i:]
                break
            count = i
        if count == n-1:
            return True
        else:
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1] or nums[i] > rotate:
                    return False
        return True

    def remove_duplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return nums
        temp = []
        for i in range(k):
            temp.append(nums.pop())
        print(nums)
        print(temp)
        for i in temp:
            nums.insert(0, i)
        return nums

    def move_zeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = 0, 0
        while i < n:
            if nums[j] == 0:
                nums.append(nums[j])
                nums.pop(j)
            else:
                j += 1
            i += 1
        print(nums)

    def search_in_sorted(self, arr, N, K):

        low = 0
        high = N
        while low < high:
            mid = math.ceil((low + high) // 2)
            if arr[mid] == K:
                return 1
            elif arr[mid] < K:
                low = mid + 1
            elif arr[mid] > K:
                high = mid
        return -1

    def find_union(self, arr1, arr2, n, m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here
        i, j = 0, 0
        result = []
        while i < n and j < m:
            if arr1[i] <= arr2[j]:
                if len(result) == 0 or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
            else:
                if len(result) == 0 or result[-1] != arr2[j]:
                    result.append(arr2[j])
                j += 1
        while i < n:
            if result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        while j < m:
            if result[-1] != arr2[j]:
                result.append(arr2[i])
            j += 1

        return result

    def missing_number(self, nums: List[int]) -> int:
        xor1, xor2 = 0, 0
        for i in range(len(nums)+1):
            xor1 = xor1 ^ i
        for i in nums:
            xor2 = xor2 ^ i
        xor = xor1 ^ xor2
        return xor

    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        i = 1
        if len(nums) == 1 and nums[0] == 0:
            return 0
        if nums[0] == 0:
            count = 0
            max_one = 0
        if nums[0] == 1:
            count = 1
            max_one = 1
        while i < len(nums):
            if nums[i] == 1 and nums[i] == nums[i-1]:
                count += 1
            elif nums[i] == 1 and nums[i] != nums[i-1]:
                count = 1
            elif nums[i] == 0 and count > max_one:
                max_one = count
                count = 0
            i += 1
        return max(max_one, count)

    def single_number(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = i
            else:
                d.pop(i)
        print(d)
        for i in d:
            return i

    def len_of_long_subarr(self, arr, n, k):
        # Complete the function
        max_length = 0
        i = 0
        while i < n:
            if arr[i] <= k:
                sum = 0
                length = 0
                for j in range(i, n):
                    sum += arr[j]
                    length += 1
                    if sum == k:
                        max_length = max(max_length, length)
                        break
                    elif sum > k:
                        break
            i += 1
        return max_length


print("\nThe Result is : ", Arrays().len_of_long_subarr(
    [19, 7, 0, -17, 8, -7, 3, 16, 6, -19, -8, 11, -19, 14, 5, -5, 1, 6, -1, 13], 20, 8))
