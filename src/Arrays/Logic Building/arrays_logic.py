class Solution:
    def findFirstZero(self):
        for i in range(self.n):
            if self.nums[i] == 0:
                return i
        return -1

    def moveZeroes(self, nums):
        self.n = len(nums)
        self.nums = nums
        j = self.findFirstZero()
        if j == -1:
            return self.nums
        for i in range(j+1, self.n):
            if self.nums[i] != 0:
                (self.nums[i], self.nums[j]) = (self.nums[j], self.nums[i])
                j += 1
        return self.nums

    def removeDuplicates(self, nums):
        i = 0
        j = i+1
        count = 0
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                count += 1
            j += 1
        return nums[0:len(nums)-count+1]

    def missingNumber(self, nums):

        d = [0] * (len(nums)+1)

        for i in nums:
            d[i] += 1

        for i in range(len(nums)+1):
            if d[i] == 0:
                return i

        return -1

    def unionArray(self, nums1, nums2):
        def unionArray(self, nums1, nums2):
        arr1_len = len(nums1)
        arr2_len = len(nums2)
        i = 0
        j = 0
        prev_ele = -256
        temp_arr = []

        while i < arr1_len and j < arr2_len:
            if nums1[i] <= nums2[j]:
                if nums1[i] != prev_ele:
                    prev_ele = nums1[i]
                    temp_arr.append(nums1[i])
                i += 1
            else:
                if nums2[j] != prev_ele:
                    prev_ele = nums2[j]
                    temp_arr.append(nums2[j])
                j += 1

        while i < arr1_len:
            if nums1[i] != prev_ele:
                prev_ele = nums1[i]
                temp_arr.append(nums1[i])
            i += 1

        while j < arr2_len:
            if nums2[j] != prev_ele:
                prev_ele = nums2[j]
                temp_arr.append(nums2[j])
            j += 1

        return temp_arr
    
    def intersectionArray(self, nums1, nums2):
        i = 0
        j = 0
        temp_arr = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                temp_arr.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return temp_arr


nums1 = [1, 2, 2, 3, 5] nums2 = [1, 2, 7]
print(Solution().unionArray(nums1, nums2))
