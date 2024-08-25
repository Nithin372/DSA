n = int(input("\nEnter the Size of the Array : "))
a = list(map(int, input("\n Enter the Array of Elements : ").split()))


class Sorting:
    def __init__(self):
        print("\n")

    def bubbleSort(self, n, a):
        print("\nExecuting Bubble sort")

        for i in range(n):
            for j in range(i):
                if a[i] < a[j]:
                    (a[i], a[j]) = (a[j], a[i])
        return a

    def selectionSort(self, n, a):
        print("\nExecuting Selection sort")

        for i in  range(n-1):
            min = i
            for j in range(i, n, 1):
                if a[j] < a[min]:
                    min = j
            (a[i], a[min]) = (a[min], a[i])

        return a
    def insertionSort(self,n,a):
        print("\nExecuting Insertion sort")
        for i in range(1,n):
            j = i
            while j>0 and a[j-1]>a[j]:
                (a[j-1],a[j]) = (a[j],a[j-1])
                j -= 1
        return a
    def mergeSort(self,low,high,a):
        mid = (low + high) // 2
        if low >= high:
            return 0
        # Dividing the Left part of the array
        self.mergeSort(low,mid,a)
        # Dividing the Right part of the array
        self.mergeSort(mid+1,high,a)
        # Merging the sub-array's
        self.merge(low,mid,high,a)
    def merge(self,low,mid,high,a):
        print("\n Executing Merge sort")
        left  = low
        right = mid+1
        i = 0
        b = []
        while left <= mid and right <= high:
            if a[left] <= a[right]:
                b.append(a[left])
                left += 1
            else:
                b.append(a[right])
                right += 1
            i += 1
        while left <= mid:
            b.append(a[left])
            left += 1
            i += 1
        while right <= high:
            b.append(a[right])
            right += 1
            i += 1
        return b
        
    


result = Sorting().mergeSort(0,n,a)
print("\n The Elements after Sorting is : ", result)

# 13 46 24 52 20 9
