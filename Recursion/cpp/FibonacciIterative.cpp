#include "FibonacciIterative.h"

FibonacciIterative::FibonacciIterative() {

}

int FibonacciIterative::calculateFibonacci(int& n) {
	cout << "This program is calculating Fibonacci(" << n << ") by iterative method.\n";
	if (n <= 1)
	{
		cout << "Fibonacci(" << n << ") is " << n << "\n";
		return n;
	}
	int f;
	int f1 = 0;
	int f2 = 1;
	cout << f1 << " " << f2 << " ";
	for (int i = 2; i <= n; i++) {
		f = f1 + f2;
		cout << f << " ";
		f1 = f2;
		f2 = f;
	}
	return f;
}