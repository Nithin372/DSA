n = int(input("\nEnter the Size of the Array : "))
a = list(map(int,input("\n Enter the Array of Elements : ").split()))

class Sorting:
    def __init__(self):
        print("\n Learning the Sorting \n")
        
    def bubbleSort(self,n,a):
        for i in range(len(n)):
            for j in range(i):
                if a[i] > a[j]:
                    (a[i],a[j]) = (a[j],a[i])
        return a
    
    
result = Sorting().bubbleSort(n,a)
print("\n The Elements after Sorting is : ",result)