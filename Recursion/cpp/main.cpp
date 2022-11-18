#include "main.h"
#include "Factorial.h"
#include "FibonacciIterative.h"
#include "FibonacciRecursive.h"

using namespace std;

int main()
{
	bool configFactorial = true;
	bool configFibonacciIterative = true;
	bool configFibonacciRecursive = true;

	if(configFactorial){
		int n;
		cout << "Enter a input number for calculating factorial: ";
		cin >> n;
		Factorial fact;
		int factorialNumber = fact.calculateFactorial(n);
		cout << "\nOutput of Factorial(" << n << ") is " << factorialNumber << "\n";
	}

	if (configFibonacciIterative) {
		int n;
		cout << "\nEnter a input number for calculating fibonacci (iterative): ";
		cin >> n;
		FibonacciIterative fibitr;
		int fibonacciNumber = fibitr.calculateFibonacci(n);
		cout << "\nOutput of Fibonacci(" << n << ") is " << fibonacciNumber << "\n";
	}

	if (configFibonacciRecursive) {
		int n;
		cout << "\nEnter a input number for calculating fibonacci (recursive): ";
		cin >> n;
		FibonacciRecursive fibrec;
		int fibonacciNumber = fibrec.calculateFibonacci(n);
		cout << "\nOutput of Fibonacci(" << n << ") is " << fibonacciNumber << "\n";
	}
	
}