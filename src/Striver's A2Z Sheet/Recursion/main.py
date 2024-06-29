n = list(map(int,input("\nEnter the Array : ").split()))
#  region Recusrsion Problems
class Recursion:
    def __init__(self):
        print("\nLearning the Recusrion\n")
        
    # region Print 1 to N using recursion
    def _1toN_(self,i,n):
        if i <= n:
            print(i,end=" ")
            Recursion._1toN_(self,i+1,n)
    
    # region Print N to 1 using recursion
    def _Nto1_(self,i,n):
        if n >= i:
            print(n,end=" ")
            Recursion._Nto1_(self,i,n-1)
            
    # region Sum of first N numbers
    def sumOfN(self,n):
        if n == 0:
            return 0
        else:
            return n + self.sumOfN(n-1)
    
    # region Factorial of N numbers
    def factorial(self,n):
        if n == 1:
            return 1
        else:
            return n*self.factorial(n-1)
    #  region Check if a string is palindrome or not
    def isPalindrome(self,n):
        left = 0
        right = len(n)-1
        while left<right:
            if n[left].lower() != n[right].lower():
                return False
            else:
                left += 1
                right -= 1  
        return True
    
    # region Fibonacci Number
    def fibonacciNumber(self,n):
        if n == 0 or n == 1:
            return 1
        else:
            return self.fibonacciNumber(n-1) + self.fibonacciNumber(n-2) 
               
    # region Reverse an array
    def reverseAnArray(self,n):
        left = 0
        right = len(n)-1
        while left < right:
            (n[left],n[right]) = (n[right],n[left])
            left += 1
            right -= 1
        return n

print(Recursion().reverseAnArray(n))