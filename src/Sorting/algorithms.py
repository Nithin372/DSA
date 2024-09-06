class Solution:
    
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n-1):
            j = i+1
            ind = i
            while j < n:
                if nums[j] < nums[ind]:
                    ind = j
                j += 1
            if ind != i:
                (nums[i],nums[ind]) = (nums[ind],nums[i])
        return nums
    
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] > nums[j]:
                    (nums[i],nums[j]) = (nums[j],nums[i])
        return nums
    
    def insertionSort(self, nums):
        n = len(nums)
        for i in range(n):
            j = i
            while j > 0 and nums[j-1]>nums[j]:
                (nums[j],nums[j-1]) = (nums[j-1],nums[j])
                j -= 1
        return nums
    
    def merge(self,arr,low,mid,high):
        temp_arr = []
        left = low
        right = mid+1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp_arr.append(arr[left])
                left += 1
            else:
                temp_arr.append(arr[right])
                right += 1
        while left <= mid:
            temp_arr.append(arr[left])
            left += 1
        while right <= high:
            temp_arr.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp_arr[i-low]

    def mergerSortCore(self,arr,low,high):
        while low >= high:
            return
        mid = (low+high) // 2
        self.mergerSortCore(arr,low,mid)
        self.mergerSortCore(arr,mid+1,high)
        self.merge(arr,low,mid,high)

    def mergeSort(self, nums):
        n  = len(nums)
        self.mergerSortCore(nums,0,n-1)
        return nums