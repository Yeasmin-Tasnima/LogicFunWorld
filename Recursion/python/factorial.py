class Factorial:
    def __init__(self):
        pass

    def calculate_factorial(self, n: int) -> int:
        print("This program is calculating Factorial({})".format(n))
        if n == 0:
            print("Factorial({}) is {}".format(n, 1))
            return 1
        f = n * self.calculate_factorial(n - 1)
        print("Factorial({}) is {}".format(n, f))
        return f
