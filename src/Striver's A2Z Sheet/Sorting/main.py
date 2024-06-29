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

        for i in range(n-1):
            min = i
            for j in range(i, n, 1):
                if a[j] < a[min]:
                    min = j
            (a[i], a[min]) = (a[min], a[i])

        return a


result = Sorting().selectionSort(n, a)
print("\n The Elements after Sorting is : ", result)

# 13 46 24 52 20 9
