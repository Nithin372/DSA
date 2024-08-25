import math

n = int(input("Enter the Number : "))
# m = int(input("Enter the Number : "))

class MathProgram:
    def __init__(self):
        print("\nLearning the Basic Maths\n")
    
    # Count digits in a number
    def countDigits(self,n):
        tmp = n
        count = 0
        while n>0:
            count += 1
            n = n//10
        # Brute Force Approach
        #print(f'The count of digits in {tmp} is {count}')
        # Optimal Approach
        #print(f'The count of digits in {tmp} is {int(math.log10(tmp))+1}')
        return count
    
    # Reverse Digits of A Number
    def reverseNumber(self,n):
        i = n
        result  = 0
        while i>0:
            result = result*10 + i%10
            i = i//10
        # Brute Force Approach
        print(f'The reversal of {n} is {result}')
        return result
       
    # Check the Palindrome
    def palindromeCheck(self,n):
        reverse = self.reverseNumber(n)
        if reverse == n:
            print(f'The Number {n} is a Palindrome...')
        else:
            print(f'The Number {n} is not a Palindrome...')
    
    # GCD or HCF
    def gcdHcf(self,n1,n2):
        hcf = 0
        # Brute Force Approach
        for i in range(1,min(n1,n2)):
            if n1%i == 0 and n2%i==0:
                hcf = i
        print(f'The GCD of {n1} & {n2} is {hcf}')
        
        #Better Approach
        for i in range(min(n1,n2),1,-1):
            if n1%i == 0 and n2%i == 0:
                print(print(f'The GCD of {n1} & {n2} is {i}'))
                break
        # Optimal Approach
        # To find the GCD of n1 and n2 where n1 > n2:
        # Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
        # Once one of them becomes 0, the other number is the GCD of the original numbers.
        pass
    
    # Armstrong Numbers
    def armstrongNumbers(self,n):
        # Brute Force Approach & Optimal Approach
        k = self.countDigits(n)
        i = n
        armstrong = 0
        while n>0:
            armstrong = (n%10)**k + armstrong
            n = n//10
        if i == armstrong:
            print(f'{i} is an Armstrong number...')
        else:
            print(f'{i} is not an Armstrong number...')
            
    # Print all Divisors of a given Number
    def printAllDivisors(self,n):
        print(f'All the Divisors of {n} is : ',end="")
        # Brute Force Approach
        for i in range(1,n+1):
            if n%i == 0:
                print(i,end=" ")
        print("\n")
        # Optimal Approach
        # if d is a divisor of n then n/d is also a divisor of n.
        print(f'All the Divisors of {n} is : ',end="")
        j = int(math.sqrt(n))
        for i in range(1,j+1):
            if n%i == 0:
                print(i,end=" ")
            if i != n//i:
                print(n//i,end=" ")
    
    # Check if a number is prime or not
    def isPrime(self,n):
        count = 0
        # Brute Force Approach
        for i in range(1,n+1):
            if n%i == 0:
                count += 1
        if count == 2:
            print(f'{n} is Prime number...')
        else:
            print(f'{n} is not a Prime number...')
            


MathProgram().isPrime(n)