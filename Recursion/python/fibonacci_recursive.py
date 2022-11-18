class FibonacciRecursive:
    def __init__(self):
        pass

    def calculate_fibonacci(self, n: int) -> int:
        print("This program is calculating Fibonacci({}) by recursive method".format(n))
        if n <= 1:
            print("Fibonacci({}) is {}".format(n, n))
            return n
        f = self.calculate_fibonacci(n - 1) + self.calculate_fibonacci(n - 2)
        print("Fibonacci({}) is {}".format(n, f))
        return f
