n = int(input("\nEnter the Number N : "))

class Recursion:
    def __init__(self):
        print("\nLearning the Recusrion\n")
        
    # Print 1 to N using recursion
    def _1toN_(self,i,n):
        if i <= n:
            print(i,end=" ")
            Recursion._1toN_(self,i+1,n)
    
    # Print N to 1 using recursion
    def _Nto1_(self,i,n):
        if n >= i:
            print(n,end=" ")
            Recursion._Nto1_(self,i,n-1)
            
    # Sum of first N numbers
    def sumOfN(self,n):
        if n == 0:
            return 0
        else:
            return n + self.sumOfN(n-1)
    
    def factorial(self,n):
        if n == 1:
            return 1
        else:
            return n*self.factorial(n-1)

print(Recursion().factorial(n))