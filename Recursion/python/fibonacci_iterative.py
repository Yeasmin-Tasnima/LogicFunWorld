class FibonacciIterative:
    def __init__(self):
        pass

    def calculate_fibonacci(self, n: int) -> int:
        print("This program is calculating Fibonacci({}) by iterative method".format(n))
        if n <= 1:
            print("Fibonacci({}) is {}".format(n, n))
            return n
        f1 = 0
        f2 = 1
        print(f1, end=" ")
        print(f2, end=" ")
        for num in range(2, n + 1):
            f = f1 + f2
            if num != n:
                print(f, end=" ")
            else:
                print(f)
            f1 = f2
            f2 = f
        # print("Factorial({}) is {}".format(n, f))
        return f
