n = int(input())
class Pattern:
    def _init_(self):
        print('\nStarting the Constructor\n')

    def str_pattern1(self,n):
        i = 1
        while i < n+1:
            j = 1
            while j <= i:
                print('*' ,end=" ")
                j += 1
            print()
            i += 1
    def str_pattern2(self,n):
        for i in range(n+1):
            print('*' * i)
        print()
    def str_pattern3(self,n):
        for i in range(n):
            for j in range(i+1):
                print(j+1,end=" ")
            print()
    def str_pattern4(self,n):
        for i in range(n):
            for j in range(i+1):
                print(i+1, end=" ")
            print()
    def str_pattern5(self,n):
        i = 0
        while i < n:
            j = n
            while j > i:
                print('*' ,end=" ")
                j -=  1
            print()
            i += 1
    def str_pattern6(self,n):
        i = 1
        while i <= n:
            j = i
            while j <= n:
                print(j, end=" ")
                j += 1
            print()
            i += 1



        
sol = Pattern()
sol.str_pattern6(n)