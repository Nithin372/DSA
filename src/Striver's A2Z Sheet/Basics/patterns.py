n = int(input('Enter yur Input : '))


class Pattern:
    def _init_(self):
        print('\nStarting the Constructor\n')

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


sol = Pattern()
sol.str_pattern_10(n)
