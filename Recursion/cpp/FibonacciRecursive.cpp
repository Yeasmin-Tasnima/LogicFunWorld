#include "FibonacciRecursive.h"

FibonacciRecursive::FibonacciRecursive() {

}

int FibonacciRecursive::calculateFibonacci(const int& n) {
	cout << "This program is calculating Fibonacci(" << n << ") by recursive method.\n";
	if (n <= 1)
	{
		cout << "Fibonacci(" << n << ") is " << n << "\n";
		return n;
	}
	int f = calculateFibonacci(n - 1) + calculateFibonacci(n - 2);
	return f;
}