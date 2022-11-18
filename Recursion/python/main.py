from factorial import Factorial
from fibonacci_iterative import FibonacciIterative
from fibonacci_recursive import FibonacciRecursive

if __name__ == '__main__':
    config_factorial = True
    config_fibonacci_iterative = True
    config_fibonacci_recursive = True

    if config_factorial:
        n = int(input("Enter a input number for calculating factorial: "))
        factorial = Factorial()
        factorial_number = factorial.calculate_factorial(n)
        print("Output of Factorial({}) is {}".format(n, factorial_number))

    if config_fibonacci_iterative:
        n = int(input("Enter a input number for calculating fibonacci (iterative): "))
        fibonacci = FibonacciIterative()
        fibonacci_number = fibonacci.calculate_fibonacci(n)
        print("Output of Fibonacci({}) is {}".format(n, fibonacci_number))

    if config_fibonacci_recursive:
        n = int(input("Enter a input number for calculating fibonacci (recursive): "))
        fibonacci = FibonacciRecursive()
        fibonacci_number = fibonacci.calculate_fibonacci(n)
        print("Output of Fibonacci({}) is {}".format(n, fibonacci_number))
