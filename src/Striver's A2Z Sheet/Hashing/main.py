n = list(map(int,input("\n Enter the Array of Elements : ").split()))

class Hashing:
    def __init__(self):
        print("\nLearning the Hashing \n")
    
    # region Counting frequencies of array elements
    def countingFrequencies(self,n):
        result = {}
        for i in n:
            if i  not in result:
                result[i] = 1
            else:
                result[i] += 1
        return result
    
    
print(Hashing().countingFrequencies(n))