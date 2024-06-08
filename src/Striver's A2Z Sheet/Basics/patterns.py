n = int(input('Enter yur Input : '))


class Pattern:
    def _init_(self):
        print('\nLearning the Different Patterns\n')

    def str_pattern_1(self, n):
        i = 1
        while i < n+1:
            j = 1
            while j <= i:
                print('*', end=" ")
                j += 1
            print()
            i += 1

    def str_pattern_2(self, n):
        for i in range(n+1):
            print('*' * i)
        print()

    def str_pattern_3(self, n):
        for i in range(n):
            for j in range(i+1):
                print(j+1, end=" ")
            print()

    def str_pattern_4(self, n):
        for i in range(n):
            for j in range(i+1):
                print(i+1, end=" ")
            print()

    def str_pattern_5(self, n):
        i = 0
        while i < n:
            j = n
            while j > i:
                print('*', end="")
                j -= 1
            print()
            i += 1

    def str_pattern_6(self, n):
        i = n
        while i >= 1:
            j = 1
            while j <= i:
                print(j, end=" ")
                j += 1
            print()
            i -= 1

    def str_pattern_7(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end="")
            for j in range(2*i+1):
                print("*", end="")
            for j in range(n-i-1):
                print(" ", end="")
            print()

    def str_pattern_8(self, n):
        for i in range(n-1, -1, -1):
            for j in range(n-i-1):
                print(" ", end="")
            for j in range(2*i+1):
                print("*", end="")
            for j in range(n-i-1):
                print(" ", end="")
            print()

    def str_pattern_9(self, n):
        self.str_pattern_7(n)
        self.str_pattern_8(n)

    def str_pattern_10(self, n):
        self.str_pattern_2(n)
        print(end="")
        self.str_pattern_5(n)
        
    def str_pattern_11(self,n):
        for i in range(n+1):
            if i%2 == 0:
                start = 0
            else:
                start = 1
            for j in range(i):
                print(start,end=" ")
                start = 1 - start
            print()
            
    def str_pattern_12(self,n):
        spaces = 2*n-1
            
        for i in range(n+1):
            for j in range(1,i+1):
                print(j,end="")
            for j in range(spaces):
                print(end=" ")
            for j in range(i,0,-1):
                print(j,end="")
            print()
            spaces -= 2
                
            
            
    def str_pattern_13(self,n):
        start = 1
        for i in range(n+1):
            for j in range(1,i):
                print(start,end=" ")
                start += 1
            print()

    def str_pattern_14(self,n):
        for i in range(n):
            start = 'A'
            for j in range(i+1):
                print(start,end="")
                start = chr(ord(start)+1)
            print()
            
    def str_pattern_15(self,n):
        for i in range(n):
            start = 'A'
            for j in range(n,i,-1):
                print(start,end="")
                start = chr(ord(start)+1)
            print()
            
    def str_pattern_16(self,n):
        start = 'A'
        for i in range(n):
            for j in range(i+1):
                print(start,end=" ")
            start = chr(ord(start)+1)
            print()
            
    def str_pattern_17(self,n):
        spaces = 2*n - 1
        for i in range(n):
            start = 'A'
            for j in range(spaces):
                print(end=" ")
            for j in range(i+1):
                print(start,end=" ")
                start = chr(ord(start)+1)
            start = chr(ord(start)-1)
            for j in range(i,0,-1):
                start = chr(ord(start)-1)                
                print(start,end=" ")                
            print()
            spaces -= 2
    
    def str_pattern_18(self,n):
        start = 'A'
        start = chr(ord(start)+n-1)
            
        for i in range(n):
            for j in range(i+1):
                print(start,end=" ")
                start = chr(ord(start)-1)
            print()
            
    def sub_pattern_19_1(self,n):
        spaces = 0
        for i in range(n):
            for j in range(n,i,-1):
                print('*',end="")
            for j in range(spaces):
                print(end=" ")
            for j in range(n,i,-1):
              print('*',end="")
            print()
            spaces += 2  
    def sub_pattern_19_2(self,n):
        spaces = 2*n - 2
        for i in range(n):
            for j in range(i+1):
                print('*',end="")
            for j in range(spaces):
                print(end=" ")
            for j in range(i+1):
              print('*',end="")
            print()
            spaces -= 2  
    def str_pattern_19(self,n):
        self.sub_pattern_19_1(n)
        self.sub_pattern_19_2(n)
        
    def str_pattern_20(self,n):
        self.sub_pattern_19_2(n)
        self.sub_pattern_19_1(n)
    


sol = Pattern()
sol.str_pattern_20(n)
