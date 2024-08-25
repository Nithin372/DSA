import math
import sys
from typing import List


class Binary_Search:
    def search(self, nums: List[int], target: int) -> int:
        left  = 0
        right = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        
        return -1
        
        
    def b_search_recusrsion(self, nums: List[int],low : int, high : int,target : int):
        if low >  high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.b_search_recusrsion(nums,mid+1,high,target)
        return self.b_search_recusrsion(nums,low,mid-1,target)
        
        
    def lower_bound(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        result = high
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                result = mid
                high = mid-1
            else:
                low = mid+1
        return result
                
                
    def upper_bound(self,nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        result = high
        while low <= high:
           mid = (low + high) // 2
           if nums[mid] > target:
               result = mid
               high = mid - 1
           else:
               low = mid + 1
        return result

    def search_insert(self, nums: List[int], target: int) -> int:
       low = 0
       high = len(nums) - 1
       result = high + 1
       while low <= high:
           mid = (low + high) // 2
           if nums[mid] >= target:
               result = mid
               high = mid - 1
           else:
               low = mid + 1
       return result
    
    def get_floor_and_ceil(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        if len(nums) == 0:
            return [-1,-1]
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target and nums[mid-1] == target:
                return [mid-1,mid]
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [-1,-1]
    def firstOccurance(self, nums: List[int], target: int) -> int:
        first = -1
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first
        
    def lastOccurance(self, nums: List[int], target: int) -> int:
        last = -1
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1] 
        first = self.firstOccurance(nums=nums,target=target)
        if first == -1: return [-1,-1]
        last = self.lastOccurance(nums=nums,target=target)
        return [first,last-1]

    def count(self,arr, x) -> int:
        first_occurance = self.firstOccurance(nums=arr,target=x)
        last_occurance = self.lastOccurance(nums=arr,target=x)
        
        return last_occurance-first_occurance+1
    
    def rotated_array_search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            if nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid -  1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
           
        return -1
    
    def findMin(self, nums: List[int]) -> int:
        result = sys.maxsize
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[mid]:
                result = min(nums[low],result)
                low  = mid + 1
            elif nums[mid] <= nums[high]:
                result = min(nums[mid],result)
                high = mid - 1
        return result
    
    def findKRotation(self, nums: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        max_num = -1
        max_ind = 0
        while low <= high:
            mid = (low + high) // 2
            if arr[low] <= arr[mid]:
                if arr[mid] >= max_num:
                    max_num = arr[mid]
                    max_ind = mid
                low  = mid + 1
            elif arr[mid] <= arr[high]:
                if arr[high] >= max_num:
                    max_num = arr[high]
                    max_ind = high
                high = mid - 1
                
        return high - max_ind
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif nums[mid-1] == nums[mid]:
                if ((mid-1)%2 == 1 and mid%2 == 0):
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] == nums[mid+1]:
                if (mid%2 == 1 and (mid+1)%2 == 0):
                    high = mid - 1
                else:
                    low = mid + 1
        
                
arr = [3,3,7,7,10,11,11]
target = 0
print("\nThe Result is : ", Binary_Search().singleNonDuplicate(arr))
